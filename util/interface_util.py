import pika
from util import global_util


def format_published_message_properties(properties):
    var_tuple = ("content_type", "content_encoding", "headers", "delivery_mode",
                 "priority", "correlation_id", "reply_to", "expiration", "message_id",
                 "timestamp", "type", "user_id", "app_id", "cluster_id")
    if properties and not isinstance(properties, dict):
        raise TypeError('properties in the request must be dictionary, '
                        ' but got %r' % (type(properties),))
    for i in var_tuple:
        locals()[i] = properties.get(i.lower(), None)

    published_properties = pika.BasicProperties(content_type=locals()["content_type"],
                                                content_encoding=locals()["content_encoding"],
                                                headers=locals()["headers"],
                                                delivery_mode=locals()["delivery_mode"],
                                                priority=locals()["priority"],
                                                correlation_id=locals()["correlation_id"],
                                                reply_to=locals()["reply_to"],
                                                expiration=locals()["expiration"],
                                                message_id=locals()["message_id"],
                                                timestamp=locals()["timestamp"],
                                                type=locals()["type"],
                                                user_id=locals()["user_id"],
                                                app_id=locals()["app_id"],
                                                cluster_id=locals()["cluster_id"])
    return published_properties


def format_request_file(param_name, file, filename=None, string_ind = False):
    """
    :param param_name: The parameter name required by the api
    :param file: The file need to be upload, should specific file's absolute path, and in this case, the string_ind should be False
                         Also can be the string, which need to write to the file, and in this case, the string_ind should be True
    :param filename: Can specify the filename
    :param string_ind: To indicate whether the file is in string format
    :return:the returned file format will be like one of below sample
    1) files = {'file': open('report.xls', 'rb')}   ---- format_request_file("file", os.path.join(PROJECT_DIR, "data", "report.xls"))
    2) files = {'file': ('report_final.xls', open('report.xls', 'rb'))}   ---- format_request_file("file", os.path.join(PROJECT_DIR, "data", "report.xls"), filename = "report_final.xls")
    3) files = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}   ---- format_request_file("file", "some,data,to,send\nanother,row,to,send\n", filename = "report_final.xls", string_ind = True)
    """
    if file is None:
        return file
    files = {param_name, open(file, 'rb')}

    if filename:
            files = {param_name, (filename, file)} if string_ind else {param_name, (filename, open(file, 'rb'))}

    return files


def format_setup_ind(setup_ind):
    if isinstance(setup_ind, dict):
        for key, value in setup_ind.items():
            global_util.set_value(key, value)