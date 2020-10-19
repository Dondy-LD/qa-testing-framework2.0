import pytest, jsonpath
from qalogger import log
from qaconfig import TestCases as tc, DataConstant as dc
from ncsqa import qadatacentral as dtc
from util.datacentral_util import ExcelUtil
from ncsqa.qainterface import InterFaceFactory
from common import qacommon
from exception.UnsupportedTypeError import UnsupportedTypeError

# ========fixture=============
def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = list(funcarglist[0]) if len(funcarglist) > 0 else funcarglist
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames] for funcargs in funcarglist], ids=[item[dc.case_id] for item in funcarglist])


class TestPrecondition:

    _predatac = dtc.get_data_central(tc.data_type, tc.precondition_clearup_path)
    _predataset = _predatac.read_data()
    _pretestdata = _predatac.convert_to_parameter(_predataset, datacols=tc.PRECON_COLS_EXCLUDE)

    params = {
        "test_precondition": _pretestdata
    }

    logging = log()

    def test_precondition(self, case_id,request_method,connection_info,request_param,
                          request_data,response_param, interaction_type,field_value,tdfield_value):
        # noinspection PyBroadException
        try:

            # Step2: Send Request and Response
            interface = InterFaceFactory.get_interface(interaction_type, request_method=request_method,
                                                       connection_info=connection_info,
                                                       request_param=request_param,
                                                       request_data=request_data,
                                                       response_param=response_param)

            # send the request
            interface.send_request()

            # receive the response
            response = interface.receive_response()

            # Step3: Replace target field value
            field_value = eval(field_value) if field_value else field_value
            if "self" in field_value:
                preselffield_value = field_value.pop("self")
                rownum = preselffield_value.pop("row")
                preselfdatac = dtc.get_data_central(tc.data_type, tc.precondition_clearup_path)
                ExcelUtil.update_testdata_for_data_preparation(preselfdatac, case_id, response, preselffield_value, tc.precondition_clearup_path, rownum=rownum)

            if field_value:
                datac = dtc.get_data_central(tc.data_type, tc.test_data_path)
                ExcelUtil.update_testdata_for_data_preparation(datac, case_id, response, field_value, tc.test_data_path)

            if tdfield_value:
                predatac = dtc.get_data_central(tc.data_type, tc.precondition_clearup_path)
                ExcelUtil.update_testdata_for_data_preparation(predatac, case_id, response, eval(tdfield_value), tc.precondition_clearup_path)

            self.logging.info("Precondition Pass ! test case %s passed" % case_id)

        except UnsupportedTypeError as err:

            self.logging.info("Precondition Fail ! test case %s failed" % case_id)

            self.logging.error(str(err), exc_info=True)

            pytest.fail()

        except Exception as e:

            self.logging.info("Precondition Fail ! test case %s failed" % case_id)

            self.logging.error(e, exc_info=True)

            pytest.fail()
