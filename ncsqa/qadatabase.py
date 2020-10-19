from ncsqa import qaconstant as con
from exception.UnsupportedTypeError import UnsupportedTypeError
from ncsqa.database.MongoDB import MongoDB
from ncsqa.database.Mssql import Mssql
from ncsqa.database.Redis import Redis


class DataBaseFactory:

    @staticmethod
    def get_database(database_type):
        if database_type not in con.SUPPORTED_DATABASE_TYPE:
            raise UnsupportedTypeError(database_type, con.SUPPORTED_DATABASE_TYPE)
        if database_type == con.DATABASE_TYPE_MONGODB:
            db_client = MongoDB()
        elif database_type == con.DATABASE_TYPE_MSSQL:
            db_client = Mssql()
        elif database_type == con.DATABASE_TYPE_REDIS:
            db_client = Redis()

        return db_client
