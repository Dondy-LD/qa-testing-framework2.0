import os,grpc
from ncsqa import qaconstant as qc

PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))


class InterfaceConstant:
    base_url = "http://192.168.200.203:30002"


class DataConstant:

    case_id = "case_id"


class LogConstant:
    all_when = "midnight"
    all_backupCount = 7

    error_when = "midnight"
    error_backupCount = 7


class RabbitmqConstant:
    mq_host = "192.168.200.203"
    mq_port = "5672"
    mq_vhost = "/vms"
    mq_username = "vmsmquser"
    mq_password = "vmsmqpassword"
    ssl_required = False
    # if ssl_required = True, then these two fields must have values
    mq_ssl_certfile = os.path.join(PROJECT_DIR, "ssl-conf", "client_certificate.pem")
    mq_ssl_keyfile = os.path.join(PROJECT_DIR, "ssl-conf", "client_key.pem")


class GRPCConstant:
    server_info = "192.168.200.202:10000"
    grpc_ind = True
    channel = grpc.insecure_channel(server_info) if grpc_ind else None


class SocketConstant:
    socket_family = qc.DEFAULT_SOCKET_FAMILY
    socket_type = qc.DEFAULT_SOCKET_TYPE_TCP
    socket_proto = 0
    tcp_host = "192.168.200.38"
    tcp_port = 1207
    receive_buffsize=1024


class MssqlConstant:
    server="172.16.35.218"
    username = "sa"
    password = "P@ssword999"
    database = "IVH_DB"
    charset = "utf8"
    as_dict = True


class RedisConstant:
    """There are 3 models for url
    redis://[:password]@host:port/db    # TCP connection
    rediss://[:password]@host:port/db   # Redis TCP+SSL connection
    unix://[:password]@/path/to/socket.sock?db=db    # Redis Unix Socket connection
    """
    url_connect_ind = True
    redis_connect_url = "redis://:vmsredispassword@192.168.200.203:6379/0"
    redis_host = ""
    redis_port = 6379
    redis_db = 0
    redis_password=""


class MongodbConstant:
    """Config the mongoDB connect parameter.
    Please notes just put the value for the fields what you want,
    otherwise please put them as empty string(For mongodb_ssl, by default is False)
    """
    # mongodb_host = "mongodb://vmsdbuser:vmsdbpassword@secure.vms.local:27017/vms-fs?authMechanism=SCRAM-SHA-256&ssl=true&ssl_ca_certs=" + os.path.join(PROJECT_DIR, "ssl-conf", "ca_certificate.pem")+"&ssl_certfile="+os.path.join(PROJECT_DIR, "ssl-conf", "client.pem")
    mongodb_host = "mongodb://secure.vms.local:27017/vms-fs"
    mongodb_port = ""
    mongodb_name = ""
    mongodb_username = "vmsdbuser"
    mongodb_password = "vmsdbpassword"
    mongodb_auth_db_name = ""
    mongodb_authMechanism = "SCRAM-SHA-1"
    mongodb_ssl = True
    mongodb_ssl_ca_certs =  os.path.join(PROJECT_DIR, "ssl-conf", "ca_certificate.pem")
    # mongodb_ssl_ca_certs =  None
    mongodb_ssl_certfile = os.path.join(PROJECT_DIR, "ssl-conf", "client.pem")


class TestCases:

    TESTDATA_COLS_EXCLUDE = [
        'executed',
        "test_result"
    ]

    PRECON_COLS_EXCLUDE = [
        'executed',
        'tdrequest_method',
        'tdconnection_info',
        'tdrequest_param',
        'tdrequest_data',
        'tdresponse_param',
        'tdinteraction_type',
        'tdexecuted'
    ]

    TRARDOWN_COLS_EXCLUDE = [
        'request_method',
        'connection_info',
        'request_param',
        'request_data',
        'response_param',
        'interaction_type',
        'field_value',
        'tdfield_value',
        'executed',
        'tdexecuted'
    ]

    data_type = "excel"
    test_data_path = os.path.join(PROJECT_DIR, "data", "test_data_framework.xls") + "&test_data"
    setup_teardown_data_path = os.path.join(PROJECT_DIR, "data", "test_data_framework.xls") + "&setup_teardown_method"
    precondition_clearup_path = os.path.join(PROJECT_DIR, "data", "test_data_framework.xls") + "&precondition_clearup"

    # Specific the cases' type need to be executed, if no cases type provided, default to execute all the test cases
    case_type_to_execute = []
