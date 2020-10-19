from socket import *
from exception.SocketConnectException import SocketConnectException
from qaconfig import SocketConstant as sc
from ncsqa.interface.InterFace import InterFace


class SocketInterface(InterFace):
    """This socket interface major to support TCP and UDP,
    For other socket family, need enhance the framework to support more
    address format and response format
    """
    def __init__(self, connection_info, request_data, response_param):
        self.socket_client = socket(self.socket_family, self.socket_type, self.socket_proto)
        self._udp_ind = False
        if sc.socket_type == SOCK_DGRAM:
            self._udp_ind = True
        self._connect_host = sc.tcp_host
        self._connect_port = sc.tcp_port

        self._request_data = request_data
        self._response_param = response_param
        self._address = (self._connect_host, self._connect_port)
        self._udp_address = self._address
        if connection_info:
            self._udp_address = connection_info.get("address", self._address)

    @property
    def socket_family(self):
        socket_family = AF_INET
        if hasattr(sc, "socket_family") and sc.socket_family:
            socket_family = sc.socket_family
        return socket_family

    @property
    def socket_type(self):
        socket_type = SOCK_STREAM
        if hasattr(sc, "socket_type") and sc.socket_type:
            socket_type = sc.socket_type
        return socket_type

    @property
    def socket_proto(self):
        socket_proto = 0
        if hasattr(sc, "socket_proto") and sc.socket_proto != 0:
            socket_proto = sc.socket_proto
        return socket_proto

    @property
    def response_buffsize(self):
        buffsize = sc.receive_buffsize
        if self._response_param:
            buffsize = self._response_param.get("buffsize", sc.receive_buffsize)
        return buffsize

    def connect_ex(self):
        """
        The function is same with connect, just will return the connect status
        if connect success, will return 0.
        else will return the error code, instead of raising exception
        :return: connect code
        """
        return self.socket_client.connect_ex(self._address)

    def connect(self):
        self.socket_client.connect(self._address)

    def send_request(self):
        if not self._udp_ind:
            self.send_request_tcp(self._request_data)
        else:
            self.send_request_udp(self._request_data)

    def send_request_tcp(self, request_message):
        connect_status = self.connect_ex()
        if connect_status:
            raise SocketConnectException(family=self.socket_family,
                                         type=self.socket_type,
                                         address=self._address,
                                         error_code=connect_status)

        self.socket_client.sendall(request_message)

    def send_request_udp(self, request_message):
        self.socket_client.sendto(request_message.encode(), self._udp_address)

    def receive_response(self):
        try:
            if not self._udp_ind:
                # for TCP, the response is string and the length <= buffsize
                response = self.socket_client.recv(self.response_buffsize)
            else:
                """for UDP, the response is (string data, address), and the length of 
                the returned data <= buffsize
                """
                response = self.socket_client.recvfrom(self.response_buffsize)
        finally:
            self.socket_client.close()

        return response

    def close(self):
        self.socket_client.close()

    @property
    def blocking(self):
        pass

    @blocking.setter
    def blocking(self, flag):
        self.socket_client.setblocking(flag)

    @property
    def sockopt(self, level, optname):
        return self.socket_client.getsockopt(level, optname)

    @sockopt.setter
    def sockopt(self, level,optname,value):
        self.socket_client.setsockopt(level,optname,value)

    @property
    def timeout(self):
        return self.socket_client.gettimeout()

    @timeout.setter
    def timeout(self, timeout):
        self.socket_client.settimeout(timeout)

