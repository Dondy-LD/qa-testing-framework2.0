import xlwt, xlrd
from xlutils.copy import copy
import jsonpath
from ncsqa import qaconstant as con
from common import qacommon
from ncsqa.qadatacentral import Excel


class ExcelUtil:

    @staticmethod
    def prepare_data_setup_teardown(test_data_path, setup_teardown_data_path):
        """
        Will base the test case ids to prepare setup_data_list and teardown_data_list
            To take the column before(and include) setup_ind as setup_data_list
            To take the column between(exclude setup_ind) setup_ind and
            teardown_ind + case_id column as teardown_data_list
        Will convert the single records to dictionary format
        :param test_data_path: To get the test case_ids list from test data sheet
        :param setup_teardown_data_path: To get and convert the setup data
                    and teardown data list from setup_teardown_data sheet
        :return:setup_data_list, teardown_data_list
        """
        test_data_case_ids = ExcelUtil.get_executed_case_ids(test_data_path)
        setup_teardown_set = Excel(setup_teardown_data_path)
        setup_teardown_cases_ids = setup_teardown_set.table.col_values(0, 1)
        setup_teardown_columns = setup_teardown_set.row_first
        setup_data_list = list()
        teardown_data_list = list()
        setup_ind_index = setup_teardown_columns.index("setup_ind")
        setup_columns = setup_teardown_columns[0:setup_ind_index+1]
        teardown_ind_index = setup_teardown_columns.index("teardown_ind")
        teardown_columns = [setup_teardown_columns[0]]
        teardown_columns.extend(setup_teardown_columns[teardown_ind_index-setup_ind_index+1: teardown_ind_index+1])
        for case_id in test_data_case_ids:
            setup_data = list()
            teardown_data = list()
            row_indexes = [idx + 1 for idx, i in enumerate(setup_teardown_cases_ids) if i == case_id]
            if row_indexes:
                for row_index in row_indexes:
                    setup_ind = setup_teardown_set.table.cell(row_index, setup_ind_index).value
                    teardown_ind = setup_teardown_set.table.cell(row_index, teardown_ind_index).value
                    if setup_ind:
                        setup_row_data = list()
                        setup_row_data.extend(setup_teardown_set.table.row_values(row_index, 0, setup_ind_index + 1))
                        setup_data_sub = dict(zip(setup_columns, setup_row_data))
                        setup_data.append(setup_data_sub)
                    if teardown_ind:
                        teardown_row_data = list()
                        row_data_sub1 = setup_teardown_set.table.cell(row_index, 0).value
                        row_data_sub2 = setup_teardown_set.table.row_values(row_index, teardown_ind_index-setup_ind_index+ 1, teardown_ind_index+1)
                        teardown_row_data.append(row_data_sub1)
                        teardown_row_data.extend(row_data_sub2)
                        teardown_data_sub = dict(zip(teardown_columns, teardown_row_data))
                        teardown_data.append(teardown_data_sub)
            setup_data_list.append(setup_data)
            teardown_data_list.append(teardown_data)

        return setup_data_list, teardown_data_list

    @staticmethod
    def update_value_to_excel(udatalist, datapath):
        excel_sheetname = None
        if con.PATH_SEPARATOR in datapath:
            excel_path_sheetname = datapath.split(con.PATH_SEPARATOR)
            excel_path = excel_path_sheetname[0]
            excel_sheetname = excel_path_sheetname[1]
        else:
            excel_path = datapath

        old_excel = xlrd.open_workbook(excel_path, formatting_info=True)
        new_excel = copy(old_excel)

        if excel_sheetname:
            ws = new_excel.get_sheet(excel_sheetname)
        else:
            ws = new_excel.get_sheet(con.DEFAULT_SHEET_INDEX)

        for data in udatalist:
            ws.write(data[0], data[1], str(data[2]), ExcelUtil.format_cell_background(str(data[2])))

        new_excel.save(excel_path)


    @staticmethod
    def format_cell_background(value):
        pattern = xlwt.Pattern()
        pattern.pattern = xlwt.Pattern.SOLID_PATTERN
        """1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,
         7 = Cyan, 16 = Maroon,17 = Dark Green, 18 = Dark Blue, 
         19 = Dark Yellow , almost brown), 20 = Dark Magenta, 21 = Teal, 
         22 = Light Gray, 23 = Dark Gray
        """
        if value.lower() == "pass":
            pattern.pattern_fore_colour = 3
        elif value.lower() == "fail":
            pattern.pattern_fore_colour = 2
        elif value.lower() == "skip":
            pattern.pattern_fore_colour = 5
        else:
            pattern.pattern_fore_colour = 1

        style = xlwt.XFStyle()
        style.pattern = pattern
        return style

    @staticmethod
    def get_executed_case_ids(test_data_path):
        executed_case_ids_list = []
        table_set = Excel(test_data_path).read_data()
        for item in table_set:
            if item.get("executed").lower() == "y":
                executed_case_ids_list.append(item.get("case_id"))
        return executed_case_ids_list

    @staticmethod
    def update_testdata_for_data_preparation(datac, case_id, response, field_value, datapath, rownum=-1):
        pendingupdate = []
        case_id_list = []
        row_num_flag = False
        """The case_id can be either string or list, 
        if need to update one precondition record  match to multiple cases, can put them in list
        """
        if isinstance(rownum, int) and rownum>0:
            case_id_list.append(rownum)
            row_num_flag = True
        elif isinstance(rownum, list):
            case_id_list = rownum
            row_num_flag = True
        elif qacommon.is_expression(case_id):
            case_id_list = eval(case_id)
        else:
            case_id_list.append(case_id)

        for key, value in field_value.items():
            for case_id in case_id_list:
                rowindex = datac.get_index_by_row_value(case_id, row_num_flag=row_num_flag)
                colindex = datac.get_index_by_column_value(key)
                olddata = eval(datac.table.cell(rowindex, colindex).value)

                for param, replaced in value.items():
                    # if response is string only, put the value as 0, will replace with the string response immediately.
                    qacommon.update_dictionary(olddata, param, replaced)
                    newdata = (rowindex, colindex, olddata)
                    pendingupdate.append(newdata)

        ExcelUtil.update_value_to_excel(pendingupdate, datapath)

    @staticmethod
    def write_result_to_test_data(datac, datapath, test_result, colunm="test_result"):
        pendingupdate = []
        for result in test_result:
            rowindex, colindex = datac.get_index_by_row_column_value(result[0], colunm)
            result = (rowindex, colindex, result[1])
            pendingupdate.append(result)
        ExcelUtil.update_value_to_excel(pendingupdate, datapath)
