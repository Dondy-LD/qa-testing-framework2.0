class MongoDBInitialException(Exception):
    def __init__(self, **kwargs):
        self._host = kwargs.get("host", "")
        self._port = kwargs.get("port", "")
        self._dbname = kwargs.get("dbname", None)
        self._username = kwargs.get("username", None)
        self._password = kwargs.get("password", None)
        self._ssl_required = kwargs.get("ssl", False)

    def __str__(self):
        return "The mongodb init connection fail(host is {host}, port is {port}, " \
               "dbname is {dbname}, username is {username}, password is {password}" \
               ", ssl_required is {ssl_required}".format(host=self._host,
                                                                            port=self._port,
                                                                            dbname=self._dbname,
                                                                            username=self._username,
                                                                            password=self._password,
                                                                            ssl_required=self._ssl_required
                                                                            )