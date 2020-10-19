import uuid
from ncsqa import qaconstant as con
from util import global_util
# import protocode
from ncsqa.interface.RestfulInterface import RestfulInterface
from ncsqa.interface.RabbitmqInterface import RabbitmqInterface
from ncsqa.interface.SocketInterface import SocketInterface
from ncsqa.interface.GRPCInterface import GRPCInterface
from exception.UnsupportedTypeError import UnsupportedTypeError


class InterFaceFactory:

    @staticmethod
    def get_interface(interaction_type, request_method=None,
                      connection_info=None,
                      request_param=None,
                      request_data=None,
                      response_param=None):

        if interaction_type not in con.SUPPORTED_INTERACTION_TYPE:
            raise UnsupportedTypeError(interaction_type, con.SUPPORTED_INTERACTION_TYPE)

        if interaction_type == con.INTERACTION_TYPE_REST:
            interface = RestfulInterface(request_method, connection_info, eval(request_data))
        elif interaction_type == con.INTERACTION_TYPE_RABBITMQ:
            interface = RabbitmqInterface(eval(connection_info), eval(request_data), response_param)
        elif interaction_type == con.INTERACTION_TYPE_SOCKET:
            interface = SocketInterface(connection_info, request_data, response_param)
        elif interaction_type == con.INTERACTION_TYPE_GRPC:
            interface = GRPCInterface(eval(connection_info), request_param, request_data, request_method)

        return interface