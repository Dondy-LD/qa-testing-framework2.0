import pymssql
from qaconfig import MssqlConstant as msc


class Mssql:
    def __init__(self):
        self._server = msc.server
        self._user = msc.username
        self._password = msc.password
        self._database = msc.database
        self._charset = msc.charset
        self._as_dict = msc.as_dict

    def _get_connect(self):
        if not self._database:
            raise(NameError, "No database info provided")

        self.connect = pymssql.connect(
            server=self._server,
            user= self._user,
            password = self._password,
            database = self._database,
            charset=self._charset,
            as_dict = self._as_dict
        )

        cursor = self.connect.cursor()

        if not cursor:
            raise(NameError, "The connection to the database fail")

        return cursor

    def find_all(self, query_sql, params=None):
        with self._get_connect() as cur:
            if isinstance(params, list):
                cur.executemany(query_sql, params)
            else:
                cur.execute(query_sql, params)

            response = cur.fetchall()

        return response

    def find_one(self, query_sql, params=None):
        with self._get_connect() as cur:
            if isinstance(params, list):
                cur.executemany(query_sql, params)
            else:
                cur.execute(query_sql, params)

            response = cur.fetchone()

        return response

    def find_many(self, query_sql, params=None,size=None):
        with self._get_connect() as cur:
            if isinstance(params, list):
                cur.executemany(query_sql, params)
            else:
                cur.execute(query_sql, params)

            response = cur.fetchmany(size)

        return response


