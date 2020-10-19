#! /usr/bin/env/python3
# _*_coding:utf-8_*_

import os
import subprocess
from ncsqa import qasummaryreport

root_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))


def run_tests():
    """
    To run all the test cases
    :return:
    """
    pre_command = "pytest -s " + os.path.join(root_path, "cases", "test_precondition.py::TestPrecondition::test_precondition")
    test_command = "pytest -s " + os.path.join(root_path, "cases", "test_cases.py::TestCases::test_cases") + " --html=" + os.path.join(root_path, "reports", "qa_testing_report.html")
    teardown_command = "pytest -s " + os.path.join(root_path, "cases", "test_teardown.py::TestTeardown::test_teardown")

    subprocess.run(pre_command, shell=True)
    subprocess.run(test_command, shell=True)
    subprocess.run(teardown_command, shell=True)


if __name__ == "__main__":
    run_tests()
    qasummaryreport.final_testing_job_result(os.path.join(root_path, "reports", "qa_testing_report.html"))  # To parse html report to get final result (True/False) of audit service testing