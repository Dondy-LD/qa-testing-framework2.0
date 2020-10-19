from pymongo import MongoClient
from exception.MongoDBInitialException import MongoDBInitialException
from qaconfig import MongodbConstant as mgc


class MongoDB:

    def __init__(self, **kwargs):
        """Initial mongoDB instance:
        :parameter
        --host:  hostname or IP address or Unix domain socket
            path of a single mongod or mongos instance to connect to, or a
            mongodb URI, or a list of hostnames / mongodb URIs
        --port: MongoDB Port, if not provided, the default value is 27017
        --db_name: Database name, if not provide, will use the default
        DB name which is implemented in client.get_database()
        --username / password: Database connect username and password,
        if provided, will do the authentication

        (1) Init an MongoDB client with host and port
        (2) Get a database with dbname
        (3) Validate username and password if provided

        Normally the MongoDB will close and release the resource
        automatically, but if hit the exception, will manually close the
        mongoDB client.

        The use is like:

        from ncsqa import KqaDataBase
        mongoDB = KqaDataBase.MongoDB(host="192.168.200.215",
        db_name="core_engine", username="core_engine",
        password="core_engine")

        """
        self._host = mgc.mongodb_host
        self._port = mgc.mongodb_port if mgc.mongodb_port else None
        self._db_name = mgc.mongodb_name if mgc.mongodb_name else None
        self._auth_db_name = mgc.mongodb_auth_db_name
        self._username = mgc.mongodb_username
        self._password = mgc.mongodb_password

        if mgc.mongodb_authMechanism:
            kwargs["authMechanism"] = mgc.mongodb_authMechanism

        if mgc.mongodb_ssl:
            kwargs["ssl"] = mgc.mongodb_ssl
            kwargs["ssl_certfile"] = mgc.mongodb_ssl_certfile
            kwargs["ssl_ca_certs"] = mgc.mongodb_ssl_ca_certs

        try:
            self.client = MongoClient(self._host, self._port, **kwargs)
            if self._username and self._password:
                if self._auth_db_name:
                    self.db = self.client.get_database(self._auth_db_name)
                elif self._db_name:
                    self.db = self.client.get_database(self._db_name)
                else:
                    self.db = self.client.get_database()
                self.db.authenticate(self._username, self._password)

            if self._auth_db_name and self._db_name:
                self.db = self.client.get_database(self._db_name)

        except Exception:
            if hasattr(self, "client") and self.client:
                self.client.close()
            raise MongoDBInitialException(host=self._host, port=self._port,
                                          dbname=self._db_name, username=self._username,
                                          password=self._password, **kwargs)

    def close(self):
        self.client.close()

    def find_one(self, collection_name, query=None, returncol=None):
        """
        Base on the query condition to search out the first record of all matched records, and return the specific columns which are included in returncol.

        :param collection_name: The name of the collection - it is a string
        :param query: The conditions that the results must match
        :param returnedcol: The fields need to be included in the results. If it is not provided, default to return all the columns
                            And the "_id" default to be returned, if not required, just add {"_id": 0}
        :return: The first record of the record list which is matched with query condition returned, and include the returnedcol

        The use is like:
            from ncsqa import qadatabase
            mongoDB = KqaDataBase.MongoDB(host="192.168.200.215", dbname="core_engine", username="core_engine", password="core_engine")

            mongoDB.find_all("Device", query = {"_id": 5}, returnedcol = {'className':1}
        """

        return_list = self.db.get_collection(collection_name).find_one(query, returncol)

        return return_list

    def find_all(self, collection_name, query=None, returncol=None):
        """
        Base on the query condition to search out all the matched records, and return the specific columns which are included in returncol.

        :param collection_name: The name of the collection - it is a string
        :param query: The conditions that the results must match
        :param returnedcol: The fields need to be included in the results. If it is not provided, default to return all the columns
                            And the "_id" default to be returned, if not required, just add {"_id": 0}
        :return: All records which is matched with query condition returned, and include the returnedcol

        The use is like:

        from ncsqa import qadatabase
        mongoDB = qadatabase.MongoDB(host="192.168.200.215", dbname="core_engine", username="core_engine", password="core_engine")

        mongoDB.find_all("Device", query = {"_id": 5}, returncol = {'className':1}
        """

        return_list = list(self.db.get_collection(collection_name).find(query, returncol))

        return return_list

    def find_records_num(self, collection_name, query=None, returncol=None):

        return_list = list(self.db.get_collection(collection_name).find(query, returncol))

        return len(return_list)

    def find_object_with_pagination(self, collection_name, query=None, returncol=None, page_index=0, page_size=1):
        total_number = self.find_records_num(collection_name, query, returncol)
        return_list = list(self.db.get_collection(collection_name).aggregate([{"$match": query},
                                                                             {"$project": returncol},
                                                                             {"$skip": page_index * page_size},
                                                                             {"$limit": page_size}
                                                                             ]))
        return total_number, return_list

    def find_object_without_pagination(self, collection_name, query=None, returncol=None):
        return_list = list(self.db.get_collection(collection_name).aggregate([{"$match": query},
                                                                             {"$project": returncol}
                                                                             ]))
        return return_list