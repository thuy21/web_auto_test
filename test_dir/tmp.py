import sys, os
from time import sleep
from os.path import dirname, abspath
from public_module.tools import xls_update
from public_module.tools import xlsx_read
from data_helper.mysql_util import *

def test():
    cursor1 = conn("116.63.68.108", "lecentMysql", "lecentMysql#1234", "gd_9081")
    config_list = query_one(cursor1, "select PrisonAreaName from prisoner where `Code`='0000001443'")
    print(config_list)
    close()

if __name__ == '__main__':
    test()