import pika,ssl, json, time
from pika.exceptions import ChannelClosed
from qaconfig import RabbitmqConstant as mqc
from util.interface_util import format_published_message_properties
from ncsqa.interface.InterFace import InterFace
from exception.InvalidRabbitmqRequestException import InvalidRabbitmqRequestException
from ncsqa import qaconstant as con


class RabbitmqInterface(InterFace):
    def __init__(self, connection_info, request_data, response_param):
        self._host = mqc.mq_host if hasattr(mqc, "mq_host") else con.DEFAULT_HOST
        self._port = mqc.mq_port if hasattr(mqc,"mq_port") else con.DEFAULT_PORT
        self._mq_username =mqc.mq_username if hasattr(mqc,"mq_username") else con.DEFAULT_USERNAME
        self._mq_password =mqc.mq_password if hasattr(mqc,"mq_password") else con.DEFAULT_PASSWORD
        self._mq_vhost = mqc.mq_vhost if hasattr(mqc,"mq_vhost") else con.DEFAULT_VIRTUAL_HOST
        self._ssl_required = mqc.ssl_required if hasattr(mqc,"ssl_required") else False

        self._request_data = json.dumps(request_data.get("data", None))
        self._request_data_properties = request_data.get("properties", None)

        self._response_param = eval(response_param) if response_param else None
        self._request_exchange = connection_info.pop("exchange", None)
        self._request_queue = connection_info.pop("queue", None)
        # if the routing key is None, will take queue name as routing key
        self._request_routing_key = connection_info.pop("routing_key", "")
        self._reply_queue_info = connection_info.pop("reply_queue", None)


        """If queue is in string format, it is queue name only(if empty string, the 
        broker will create a unique queue name), others info will keep as 
        default
        if queue is in dictionary format, the related key should exactly equal 
        with queue, passive,  durable, exclusive, auto_delete
        """
        self._response_queue = ""

        """Similar with queue. If exchange is in string format, it is exchange 
        name only, others info will keep as default
        if exchange is in dictionary format, the related key should exactly equal 
        with exchange, exchange_type,  passive, durable, auto_delete,internal
        """

        """ The binding key can be String or None(rabbitmq will take queue 
        name as binding key), also can be list for topic model
        if the binding key is None or string, will be convert to list by system
        """
        self._routing_key = connection_info.get("routingkey", None)

        self._connection = self.mq_connection()
        self._channel = self.mq_channel()

        self._ch = None
        self._method = None
        self._properties = None
        self._body = None


    def mq_connection(self):
        """
        This method to finish the basic operation for mq connect:
        1. Create mq connection(with/o SSL --- based on the configuration)
        2.Create one channel
        3. Declare the queue
        4. Declare the exchange
        5. Bind the queue and exchange
        :return:
        """
        if not hasattr(self, "_connection") or self._connection.is_closed:
            credentials = pika.PlainCredentials(self._mq_username, self._mq_password)
            ssl_options = pika.ConnectionParameters.DEFAULT_SSL_OPTIONS
            if self._ssl_required:
                context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
                context.load_cert_chain(mqc.mq_ssl_certfile, mqc.mq_ssl_keyfile)
                ssl_options = pika.SSLOptions(context)
            parameters = pika.ConnectionParameters(host=self._host,
                                                   port=self._port,
                                                   credentials=credentials,
                                                   virtual_host=self._mq_vhost,
                                                   ssl_options=ssl_options)
            # 1. Create mq connection(with/o SSL --- based on the configuration)
            connection = pika.BlockingConnection(parameters)
            return connection

    def mq_channel(self):
        if not hasattr(self, "_channel") or self._channel.is_closed:
            # 2.Create one channel
            channel = self._connection.channel()
        else:
            channel = self._channel
        return channel

    def is_exchange_exist(self, exchange_name, exchange_type):
        try:
            if len(exchange_name) == 0:
                return False

            self._channel.exchange_declare(exchange=exchange_name, exchange_type=exchange_type, passive=True)
            return True
        except ChannelClosed:
            return False

    def is_queue_exists(self, queue_name):
        try:
            if len(queue_name) == 0:
                return False

            self._channel().queue_declare(queue=queue_name, passive=True)
            return True
        except ChannelClosed:
            return False

    def create_exchange(self, **kwargs):
        self._channel.exchange_declare(exchange=kwargs.get("exchange_name", ""),
                                       exchange_type=kwargs.get("exchange_type", "direct"),
                                       passive=kwargs.get("exchange_passive", False),
                                       durable=kwargs.get("exchange_durable", False),
                                       auto_delete=kwargs.get("exchange_auto_delete", False),
                                       internal=kwargs.get("exchange_internal", False))

    def create_queue(self, **kwargs):
        result = self._channel.queue_declare(kwargs.get("queue_name", ""),
                                             passive=kwargs.get("queue_passive", False),
                                             durable=kwargs.get("queue_durable", False),
                                             exclusive=kwargs.get("queue_exclusive", False),
                                             auto_delete=kwargs.get("queue_auto_delete", False))

        if len(kwargs.get("queue_name", "")) == 0:
            self._response_queue = result.method.queue

    def binding_exchange_with_queue(self, exchange_name, queue_name,
                                    binding_keys = ""):
        if isinstance(binding_keys, str):
            binding_keys = [binding_keys]

        for binding_key in binding_keys:
            self._channel.queue_bind(queue=queue_name,
                                     exchange=exchange_name,
                                     routing_key=binding_key)

    def get_message_from_queue(self, queue_name, ack):
        method, properties, body = self._channel.basic_get(queue=queue_name)

        if not (method and properties and body):
            return None, None, None
        else:
            delivery_data = {
                "delivery_tag": method.delivery_tag,
                "redelivered": method.redelivered,
                "exchange": method.exchange,
                "routing_key": method.routing_key,
                "message_count": method.message_count
            }

            message_properties = {
                "content_type": properties.content_type,
                "content_encoding": properties.content_encoding,
                "headers": properties.headers,
                "delivery_mode": properties.delivery_mode,
                "priority": properties.priority,
                "correlation_id": properties.correlation_id,
                "reply_to": properties.reply_to,
                "expiration": properties.expiration,
                "message_id": properties.message_id,
                "timestamp": properties.timestamp,
                "type": properties.type,
                "user_id": properties.user_id,
                "app_id": properties.app_id,
                "cluster_id": properties.cluster_id
            }

            if ack:
                delivery_tag = delivery_data['delivery_tag']
                self._channel.basic_ack(delivery_tag=delivery_tag)
            return delivery_data, message_properties, body

    def prepare_request_connection(self, request_data_properties):
        """
        Determine the exchange / routing_key / reply_to queue, and declare
        the related exchange if provided exchange info in the request data

        if reply_to queue is "random", will use the random queue name
        generated by rabbitmq server, and replace it in the request properties

        return the final exchange, routing_key and final request properties
        """
        exchange_name = self._request_exchange.get("exchange_name", "") if self._request_exchange else None
        exchange_type = self._request_exchange.get("exchange_type", "direct") if self._request_exchange else None
        routing_key = self._request_routing_key
        queue_name = self._request_queue.get("queue_name", "") if self._request_queue else None
        if self._request_exchange and exchange_name:
            if exchange_type in ["direct", "topic"] and len(routing_key) == 0:
                raise TypeError(f'The routing key is required when exchange_type is direct or topic')

            if not self.is_exchange_exist(exchange_name, exchange_type):
                self.create_exchange(**self._request_exchange)

        elif self._request_queue and queue_name:
            if not self.is_queue_exists(queue_name):
                self.create_queue(**self._request_queue)
            exchange_name = ""
            routing_key = queue_name
        else:
            raise InvalidRabbitmqRequestException(request_exchange = self._request_exchange,
                                                  request_queue = self._request_queue)

        reply_to = request_data_properties.get("reply_to", "")
        if len(reply_to) == 0:
            reply_to = self._reply_queue_info

        if request_data_properties and reply_to:
            reply_to = reply_to.split("/")

            if reply_to[0] == "random" or len(reply_to) == 2:
                self.create_queue(queue="", queue_exclusive=True)
            else:
                self._response_queue = reply_to[0]

            if len(reply_to) == 2:
                response_exchange_name = reply_to[0]
                response_routing_key = reply_to[1]
            else:
                response_exchange_name = exchange_name
                response_routing_key = ""

            self.binding_exchange_with_queue(response_exchange_name, self._response_queue,
                                             binding_keys=response_routing_key)
            request_data_properties["reply_to"] = self._response_queue


        return exchange_name, routing_key, request_data_properties

    def consume_response_queue(self):
        self._channel.basic_consume(self._response_queue,
                                    self.mq_callback,
                                    auto_ack=self._response_param.get("auto_ack", False) if isinstance(
                                        self._response_param, dict) else False,
                                    exclusive=self._response_param.get("exclusive", False) if isinstance(
                                        self._response_param, dict) else False,
                                    consumer_tag=self._response_param.get("consumer_tag", None) if isinstance(
                                        self._response_param, dict) else None,
                                    arguments=self._response_param.get("arguments", None) if isinstance(
                                        self._response_param, dict) else None)

    def send_request(self):
        exchange_name, routing_key, request_data_properties =self.prepare_request_connection(self._request_data_properties)

        properties = None
        if self._request_data_properties is not None:
            properties = format_published_message_properties(request_data_properties)
        self._channel.basic_publish(exchange=exchange_name,
                                    routing_key=routing_key,
                                    body=self._request_data,
                                    properties=properties)


    def receive_response(self):
        try:
            self.consume_response_queue()
            count = 0
            while self._body is None:
                self._connection.process_data_events()
                time.sleep(0.01)
                count += 1
                if count > 100:
                    raise Exception("Server no response in 1 second")
            return self._ch, self._method, self._properties, self._body
        finally:
            self.close()

    def mq_callback(self, ch, method, props, body):
        self._ch = ch
        self._method = method
        self._properties = props
        self._body = body
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def close(self):
        self.close_channel()
        self.close_connection()

    def close_connection(self):
        if hasattr(self, "_connection") and not self._connection.is_closed:
            self._connection.close()

    def close_channel(self):
        if hasattr(self, "_channel") and not self._channel.is_closed:
            self._channel.close()