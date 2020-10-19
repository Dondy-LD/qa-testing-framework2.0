
def update_dictionary(dict_data,key,value):
    if key in dict_data:
        dict_data.update({key:value})
    for dict_data_sub in dict_data.values():
        if isinstance(dict_data_sub,dict):
            update_dictionary(dict_data_sub, key,value)


def is_expression(content):
    try:
        eval(content)
    except SyntaxError:
        return False
    return True


def db_operation(dboperation, response):
    pass