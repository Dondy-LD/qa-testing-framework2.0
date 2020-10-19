class InvalidRabbitmqRequestException(Exception):
    def __init__(self, **kwargs):
        self._request_exchange = kwargs.get("request_exchange", "")
        self._request_queue = kwargs.get("request_queue", "")

    def __str__(self):
        return f"Either the exchange_name or queue_name should be provided when sending the request to rabbitmq"