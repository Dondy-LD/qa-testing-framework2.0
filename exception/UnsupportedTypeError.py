class UnsupportedTypeError(Exception):
    def __init__(self, passed_type, supported_type):
        self._passed_type = passed_type
        self._supported_type_list = supported_type

    def __str__(self):
        return f"The passed type {self._passed_type} is not" \
               f" in the supported type list({self._supported_type_list})"