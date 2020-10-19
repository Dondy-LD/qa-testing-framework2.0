from ncsqa.qadatabase import DataBaseFactory
from ncsqa import qaconstant as con

db_client = DataBaseFactory.get_database(con.DATABASE_TYPE_MSSQL)


def special_validation(case_type, response, expected_statuscd, expected_response, validation_query, expected_validation_result):
    if case_type == "add_device":
        validate_add_device(response)


def validate_add_device(response):
    db_client.find_object_without_pagination()