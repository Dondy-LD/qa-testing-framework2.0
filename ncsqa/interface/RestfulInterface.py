import requests, json
from qaconfig import InterfaceConstant as ic
from util.interface_util import format_request_file
from ncsqa.interface.InterFace import InterFace


class RestfulInterface(InterFace):

    def __init__(self, method, connection_info, request_data):
        self._method = method
        self._path = ic.base_url + connection_info
        self._request_data = request_data

    @property
    def path(self):
        path = self._path
        if "path" in self._request_data:
            path_param = self._request_data.get("path")
            for key, value in path_param.items():
                path = path.replace(key, str(value))
        return path

    @property
    def headers(self):
        headers = None
        if "headers" in self._request_data:
            headers = self._request_data.get("headers")
        return headers

    @property
    def param(self):
        params = None
        if "param" in self._request_data:
            params = self._request_data.get("param")
        return params

    @property
    def json_data(self):
        json_data = None
        if "json-data" in self._request_data:
            json_data = self._request_data.get("json-data")
        return json_data

    @property
    def form_data(self):
        form_data = None
        if "form-data" in self._request_data:
            form_data = self._request_data.get("form-data")
        return form_data

    @property
    def files(self):
        files = None
        if "files" in self._request_data:
            files = format_request_file(self._request_data.get("files"))
        return files

    @property
    def status_ok(self):
        return requests.codes.ok

    @property
    def responseurl(self):
        return self._response.url

    @property
    def responsestatuscd(self):
        return self._response.status_code

    @property
    def responseheader(self):
        return self._response.headers

    @property
    def responsetext(self):
        # The response is in Unicode format, normally for text file
        return self._response.text

    @property
    def responsecontent(self):
        """The response is in bytes format, normally for image or file,
        and will display characters for Chinese
        """
        return self._response.content

    @property
    def responsejson(self):
        """
        The built-in JSON decoder
         Need to make sure the response is defined in Json format,
         otherwise, will throw out the exception
        """
        try:
            return self._response.json()
        except json.JSONDecodeError:
            return None

    def responseerrorstatus(self):
        return self._response.raise_for_status()

    def receive_response(self):
        self._response = requests.request(self._method, self.path,
                                          params=self.param, data=self.form_data,
                                          headers=self.headers, json=self.json_data,
                                          files=self.files)
        response_dict = dict(status = self.responsestatuscd,
                                            headers=self.responseheader,
                                            text=self.responsetext,
                                            json=self.responsejson,
                                            content = self.responsecontent
                             )

        return response_dict