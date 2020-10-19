from ncsqa import qaconstant as qc


class SocketConnectException(Exception):
    def __init__(self, **kwargs):
        self._family = kwargs.get("family", qc.DEFAULT_SOCKET_FAMILY)
        self._type = kwargs.get("type", qc.DEFAULT_SOCKET_TYPE_TCP)
        self._connect_address = kwargs.get("address", None)
        self._error_code = kwargs.get("error_code", 1)


    def __str__(self):
        return "The socket connection fail, the error code is {error_code}" \
               "connection family is {family}, socket type is {type}, " \
               "connect address  is {address}".format(error_code=self._error_code,
                                                                            family=self._family,
                                                                            type=self._type,
                                                                            address=self._connect_address
                                                                            )