import pytest
from util.datacentral_util import ExcelUtil
from qalogger import log
from qaconfig import TestCases as tc, DataConstant as dc
from ncsqa import qadatacentral as dtc
from ncsqa.qainterface import InterFaceFactory
from validation import specialvalidation
from common import qacommon as common
from util import global_util, interface_util


# ========fixture=============
def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = list(funcarglist[0]) if len(funcarglist) > 0 else funcarglist
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames] for funcargs in funcarglist], ids=[item[dc.case_id] for item in funcarglist])


class TestCases:

    # Step1: Get test data
    _datac = dtc.get_data_central(tc.data_type, tc.test_data_path)
    _dataset = _datac.read_data()
    _testdata = _datac.convert_to_parameter(_dataset)

    setup_data_list, teardown_data_list = ExcelUtil.prepare_data_setup_teardown(tc.test_data_path, tc.setup_teardown_data_path)
    logging = log()
    all_test_results = []

    params = {
        "test_cases": _testdata
    }

    def teardown_class(self):
        ExcelUtil.write_result_to_test_data(self._datac, tc.test_data_path, self.all_test_results)

    def setup_method(cls):
        global_util.init()
        try:
            setup_data = cls.setup_data_list.pop(0)
            if setup_data:
                #call interface method
                for setup_data_sub in setup_data:
                    if setup_data_sub.get("setup_interaction_type"):
                        interface = InterFaceFactory.get_interface(setup_data_sub.get("setup_interaction_type"),
                                                                   request_method=setup_data_sub.get("setup_request_method"),
                                                                   connection_info=setup_data_sub.get("setup_connection_info"),
                                                                   request_param=setup_data_sub.get("setup_request_param"),
                                                                   request_data=setup_data_sub.get("setup_request_data"),
                                                                   response_param=setup_data_sub.get("setup_response_param"))
                    # send the request
                    interface.send_request()

                    # receive the response
                    response = interface.receive_response()

					# put the setup result check, if fail, can set the global value setup_fail to True
                    # if response.status_code != 200:
                    #     global_util.set_value("setup_fail", True)

                    try:
                        setup_data_ind = setup_data_sub.get("setup_ind")
                        setup_data_ind = eval(setup_data_ind)
                    except SyntaxError:
                        cls.logging.info("The setup ind format is string, no need to convert!")

                    interface_util.format_setup_ind(setup_data_ind)

                    common.db_operation(setup_data_sub.get("setup_dboperation"), response)

        except Exception as e:
            cls.logging.info(f"Setup function for case {setup_data} fail !" )
            cls.logging.error(e, exc_info=True)
            global_util.set_value("setup_fail", True)

    def teardown_method(cls):
        teardown_data = cls.teardown_data_list.pop(0)
        if teardown_data:
            # call interface method
            for teardown_data_sub in teardown_data:
                interface = InterFaceFactory.get_interface(teardown_data_sub.get("teardown_interaction_type"),
                                                           request_method=teardown_data_sub.get("teardown_request_method"),
                                                           connection_info=teardown_data_sub.get("teardown_connection_info"),
                                                           request_param=teardown_data_sub.get("teardown_request_param"),
                                                           request_data=teardown_data_sub.get("teardown_request_data"),
                                                           response_param=teardown_data_sub.get("teardown_response_param"))
                # send the request
                interface.send_request()

                # receive the response
                response = interface.receive_response()
                common.db_operation(teardown_data_sub.get("teardown_dboperation"), response)

    def test_cases(self, case_id,  case_purpose, request_method,
                   connection_info, request_param, request_data, response_param,
                   expected_statuscd, expected_response, validation_query,
                   expected_validation_result, interaction_type, case_type):
        # noinspection PyBroadException
        try:
            test_result = "Pass"

            self.logging.debug(f"the setup_fail indicator is {global_util.get_value('setup_fail', False)}")
            if global_util.get_value("setup_fail", False):
                test_result = "Skip"
                pytest.skip("The related setup function fail, so skip the corresponding case execute")

            # Step2:  Send request and get response
            # Initial interface object
            interface = InterFaceFactory.get_interface(interaction_type, request_method=request_method,
                                                       connection_info=connection_info,
                                                       request_param=request_param,
                                                       request_data=request_data,
                                                       response_param=response_param)
            # send the request
            interface.send_request()

            # receive the response
            response = interface.receive_response()

            self.logging.debug("the response for case %s is %s" % (case_id, response))

            # Step3: Get response to do common validation

            # comvalidation.common_validation(response, expected_statuscd)

            # Step4: Special validation base on caseType

            specialvalidation.special_validation(case_type, response, expected_statuscd,
                                                 expected_response, validation_query, expected_validation_result)

            self.logging.info("Cases Pass ! %s:%s passed" % (case_id, case_purpose))

        except AssertionError as error:

            self.logging.info("Cases Fail ! %s:%s failed, the actual result is different with expected result" % (case_id, case_purpose))

            self.logging.error(error)

            test_result = "Fail"

            pytest.fail()

        except Exception as e:

            self.logging.info("Cases Fail ! %s:%s failed,  some error hit in test scripts, please contact QA team for more help!" % (case_id, case_purpose))

            self.logging.error(e, exc_info=True)

            test_result = "Fail"

            pytest.fail()

        finally:
            result = (case_id,test_result)
            self.all_test_results.append(result)

