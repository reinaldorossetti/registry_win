from xlrd import open_workbook, xldate
from os import getcwd
from datetime import datetime

start = datetime.now()

"""
Need install pack XLRD:
pip install xlrd
"""

def read_excel(file):
    # get path in folder, and replace subfolder.
    path = getcwd().replace("modules","")
    path = "{}data\\{}".format(path, file)
    print(path)
    workbook  = open_workbook(path, encoding_override="utf-8")
    sheet = workbook.sheet_by_index(0)

    # read the columns name.
    keys = [(sheet.cell(0, col_index).value).lower()
                for col_index in range(sheet.ncols)]

    print("Colunas", keys)
    print("Numeros de Linhas:{}".format(sheet.nrows))
    dict_test = []
    line_values = []

    for row_index in range(1, sheet.nrows):
        for col_index in range(sheet.ncols):
            value_plan = sheet.cell(row_index, col_index).value
            if "data" in (keys[col_index]):
                # Converting to data in Brazilian format and then added to the list.
                value_plan = xldate.xldate_as_datetime(value_plan, workbook.datemode)
                value_plan = ("{:%d/%m/%Y}".format(value_plan))
                line_values.append(value_plan)
            else:
                line_values.append(value_plan)

        # A dictionary within the list, the enumerate function will place the index.
        dict_test.append(dict(enumerate(line_values)))
        line_values.clear()
    return dict_test

dic = (read_excel("seu arquivo excel"))

# By looping in the list, you can access the values by index.
for x in dic:
    print(x[0])

print(datetime.now() - start)
