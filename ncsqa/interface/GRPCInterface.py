import importlib
from qaconfig import GRPCConstant as gc
from ncsqa.interface.InterFace import InterFace
import protocode

class GRPCInterface(InterFace):
    def __init__(self, connection_info, request_param, request_data, request_method):
        self._grpc_client = connection_info.get("grpc_client")
        self._grpc_server = connection_info.get("grpc_server")
        self._grpc_stub = connection_info.get("grpc_server_stub")
        self._request_method = request_method
        self._request_param = request_param
        self._request_data = eval(request_data) if request_data else ""

        ip_module = importlib.import_module(self._grpc_client)
        self._rpc_request = getattr(ip_module, self._request_param)()

    @property
    def stub(self):
        return getattr(self._grpc_server, self._grpc_stub)(gc.channel)

    @staticmethod
    def prepare_request_data(rpc_request, request_data):
        """
        request data may include below format:
        1) scalar format, e.g: String, Int, Bool etc.
        2) Other message type
        3) Stream
        Also need to support single  and repeated for 1~2
        """

        if not isinstance(request_data, dict):
            return rpc_request

        for param, value in request_data.items():
            if isinstance(value, dict):
                for sub_param, sub_value in value.items():
                    setattr(getattr(rpc_request, param), sub_param, sub_value)
            elif isinstance(value, list) and len(value)>0 and isinstance(value[0], dict):
                    for sub_obj in value:
                        params = getattr(getattr(rpc_request, param), "add")()
                        for sub_param, sub_value in sub_obj.items():
                            setattr(params, sub_param, sub_value)
            else:
                    setattr(rpc_request, param, value)

        return rpc_request

    def send_request(self):
        if self._request_data:
            self._rpc_request = self.prepare_request_data(self._rpc_request, self._request_data)

    def receive_response(self):
        response = getattr(self.stub, self._request_method)(self._rpc_request)
        return response