import xlrd
from ncsqa import qaconstant as con
from qaconfig import TestCases as tc

"""
It is simple factory pattern.
From client side, they only need provide the filetype and filepath. 

The supported filetype is:
    (1)excel
    (2)yaml 
    (3)xml
    (4)db
"""


def get_data_central(filetype, path):
    if filetype == con.FILE_TYPE_EXCEL:
        dtc = Excel(path)
    elif filetype == con.FILE_TYPE_YAML:
        dtc = Yaml(path)
    elif filetype == con.FILE_TYPE_XML:
        dtc = Xml(path)
    elif filetype == con.FILE_TYPE_DB:
        dtc = DB(path)
    # TODO -- exception handle if no filetype match
    return dtc


"""
It is father class, will put the common method for data central process.
And these methods can be used by child
"""


class DataCentral:

    """
    For pytest cases execution, the parameter need to be a list.
    So this method is to provide the function to convert the data to the cases execution format.
    :param dataset -- the data set to filter the data
    :return
    """

    def convert_to_parameter(self, dataset, clearup_ind = False, datacols=None):
        testdataset = []

        casetypes = tc.case_type_to_execute
        if datacols is None:
            datacols = tc.TESTDATA_COLS_EXCLUDE

        for item in dataset:
            executed = item.get("tdexecuted") if clearup_ind else item.get("executed")
            if executed and executed.lower() == "y":
                if casetypes and item.get("case_type") and item.get("case_type") not in casetypes:
                    continue;
                else:
                    subitem = {key: value for key, value in item.items() if key not in datacols}
                    testdataset.append(subitem)

        return testdataset


class Excel(DataCentral):

    """
    if need to specify the sheetname,  append the sheetname to the filepath with "&"
    For example:
        the excel path of the file is "D:\test\testdata.xls"
        the sheetname is "testdata"
        the path should be "D:\test\testdata.xls&testdata"

    if no need to specify the sheetname, just pass the excel path, will get the 1st sheet by default
    """



    def __init__(self, path):

        self._table = None
        self.table = path

        # retrieve the 1st row data
        self.row_first = self.table.row_values(0)

        # retrieve the 1st column data
        self.col_first = self.table.col_values(0)

        # retrieve the total row number
        self.rowNum = self.table.nrows

        # retrieve the total col number
        self.colNum = self.table.ncols

    @property
    def table(self):
        return self._table

    @table.setter
    def table(self, path):
        if con.PATH_SEPARATOR in path:

            excel_path_sheetname = path.split(con.PATH_SEPARATOR)
            excel_path = excel_path_sheetname[0]
            excel_sheetname = excel_path_sheetname[1]

            table = xlrd.open_workbook(excel_path, formatting_info=True).\
                                                        sheet_by_name(excel_sheetname)
        else:
            table = xlrd.open_workbook(path, formatting_info=True).\
                                        sheet_by_index(con.DEFAULT_SHEET_INDEX)

        self._table = table

    def read_data(self):
        """Convert the excel data to a list which is combined by the dictionaries.
        For example:
            excel is like below
                name    age
                 dog     16
                 cat     18
            the returned list will be: [{"name":"dog", "age":"16"}, {"name":"cat", "age":"18"}]
        """
        if self.rowNum <= 1:
            print("the total rownum is less than 1")
        else:
            data_list = []
            j = 1
            for i in range(self.rowNum - 1):
                t = {}
                # get the value from 2nd line
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    t[self.row_first[x]] = values[x]

                data_list.append(t)
                j += 1

            return data_list

    def get_index_by_row_value(self, row_value, row_num_flag = False):
        if row_num_flag:
            rowindex = row_value - 1
        else:
            colval = self.table.col_values(0)
            rowindex = colval.index(row_value)

        return rowindex

    def get_index_by_column_value(self, col_value, col_num_flag = False):
        if col_num_flag:
            colindex = col_value - 1
        else:
            rowval = self.table.row_values(0)
            colindex = rowval.index(col_value)

        return colindex

    def get_index_by_row_column_value(self, row_value, col_value):

        return self.get_index_by_row_value(row_value), self.get_index_by_column_value(col_value)

    def __str__(self):
        return "Excel.."


class Yaml(DataCentral):

    def __init__(self, path):
        print("hello, this is init method for yaml")

    def read_data(self):
        print("hello, this is read_data for yaml")

    def __str__(self):
        print("hello, this is drcription for yaml")


class DB(DataCentral):

    def __init__(self, path):
        print("hello, this is init method for DB")

    def read_data(self):
        print("hello, this is read_data for DB")

    def __str__(self):
        print("hello, this is drcription for DB")


class Xml(DataCentral):
    def __init__(self, path):
        print("hello, this is init method for XML")

    def read_data(self):
        print("hello, this is read_data for XML")

    def __str__(self):
        print("hello, this is drcription for XML")
