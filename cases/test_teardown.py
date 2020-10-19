import pytest
from qalogger import log
from qaconfig import TestCases as tc, DataConstant as dc
from ncsqa import qadatacentral as dtc
from ncsqa.qainterface import InterFaceFactory

# ========fixture=============
def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = list(funcarglist[0]) if len(funcarglist) > 0 else funcarglist
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames] for funcargs in funcarglist], ids=[item[dc.case_id] for item in funcarglist])

class TestTeardown:
    _predatac = dtc.get_data_central(tc.data_type, tc.precondition_clearup_path)
    _predataset = _predatac.read_data()
    _tdtestdata = _predatac.convert_to_parameter(_predataset, clearup_ind = True, datacols=tc.TRARDOWN_COLS_EXCLUDE)

    params = {
        "test_teardown": _tdtestdata
    }

    logging = log()

    def test_teardown(self, case_id, tdrequest_method,tdconnection_info,
                      tdrequest_param,tdrequest_data,tdresponse_param,
                      tdinteraction_type):
        # Step2: Send Request and Response
        try:
            # Initial interface object
            interface = InterFaceFactory.get_interface(tdinteraction_type,
                                                       request_method=tdrequest_method,
                                                       connection_info=tdconnection_info,
                                                       request_param=tdrequest_param,
                                                       request_data=tdrequest_data,
                                                       response_param=tdresponse_param)
            # send the request
            interface.send_request()

            # receive the response
            response = interface.receive_response()

            self.logging.info("Teardown Pass ! test case {case_id} passed, the "
                              "response is {response}".format(case_id = case_id,
                                                              response=response))

        except Exception as e:

            self.logging.info("Teardown Fail ! test case {case_id}  failed".format(case_id=case_id))

            self.logging.error(e, exc_info=True)

            pytest.fail()