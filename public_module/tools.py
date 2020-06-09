from xlutils.copy import copy
import xlrd
from openpyxl import load_workbook


def xlsx_read(dir, sheet):
    """读取exel文件"""
    list = []
    wb = load_workbook(dir)
    ws = wb[sheet]
    for i in range(2, ws.max_row + 1):
        for j in range(1, ws.max_column + 1):
            if ws.cell(i, j).value != None:
                list.append(ws.cell(i, j).value)
    return list


def xls_update(dir, list, row):
    """修改excl文件"""
    book1 = xlrd.open_workbook(dir, formatting_info=True)
    book2 = copy(book1)
    sheet = book2.get_sheet(0)
    for i in range(0, len(list)):
        sheet.write(row, i, list[i])

    book2.save(dir)


if __name__ == "__main__":
    list = xlsx_read("import.xlsx")
    print(list)
    xls_update('./tmp_file/资金上账模板.xls', list)
