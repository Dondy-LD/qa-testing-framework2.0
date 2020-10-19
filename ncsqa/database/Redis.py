from redis import StrictRedis, ConnectionPool
from qaconfig import RedisConstant as rc

class Redis:
    def __init__(self):
        self._host = rc.redis_host if hasattr(rc, "redis_host") else "localhost"
        self._port = rc.redis_port if hasattr(rc, "redis_port") else 6379
        self._db = rc.redis_db if hasattr(rc, "redis_db") else 0
        self._password = rc.redis_password if hasattr(rc, "redis_password") else None
        self._url = rc.redis_connect_url if hasattr(rc, "redis_connect_url") else None

        if hasattr(rc, "url_connect_ind") and rc.url_connect_ind:
            self._pool = ConnectionPool.from_url(self._url)
        else:
            self._pool = ConnectionPool(host=self._host,
                                        port=self._port,
                                        db=self._db,
                                        password=self._password)

        self.redis_con = StrictRedis(connection_pool=self._pool)

    def string_get(self, key, value=None, start=None, end=None):
        returned_value = ""

        if isinstance(key, list):
            returned_value = self.redis_con.mget(key)
        elif value:
            returned_value = self.redis_con.getset(key, value)
        elif start is not None and end is not None:
            returned_value = self.redis_con.getrange(key, start, end)

        return returned_value

    def hash_exists(self, key, field):
        return self.redis_con.hexists(key, field)

    def hash_get(self, key, field=None):
        if field:
            returned_value = self.redis_con.hmget(key, field)
        else:
            returned_value = self.redis_con.hgetall(key)
        return returned_value

    def list_get(self, key, index=None, start=None, stop=None, length=False):
        returned_value = ""
        if index:
            returned_value = self.redis_con.lindex(key, index)
        elif start is not None and stop is not None:
            returned_value = self.redis_con.lrange(key, start, stop)
        elif length:
            returned_value = self.redis_con.llen(key)

        return returned_value

    def set_get(self, key, diff=False, inter=False, union=False, destination=None, is_member=None):
        returned_value = self.redis_con.smembers(key)
        if diff:
            returned_value = self.redis_con.sdiff(key)
            if destination:
                returned_value = self.redis_con.sdiffstore(destination, key)
        elif inter:
            returned_value = self.redis_con.sinter(key)
            if destination:
                returned_value = self.redis_con.sinterstore(destination, key)
        elif union:
            returned_value = self.redis_con.sunion(key)
            if destination:
                returned_value = self.redis_con.sunionstore(destination, key)
        elif is_member:
            returned_value = self.redis_con.sismember(key, is_member)

        return returned_value


