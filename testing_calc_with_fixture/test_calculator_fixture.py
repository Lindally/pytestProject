import sys

sys.path.append("..")

# 导入计算器的类
from pythoncode.Calculator import Calculator

# 导入获取数据的类
# from testing_calculator import get_datas_function as datas

import pytest
import yaml


class TestCalc:

    def test_add_int(self, get_instance, get_datas_with_fixture_add_int):
        data = get_datas_with_fixture_add_int
        assert data[2] == data[0] + data[1]

    def test_add_float(self, get_instance, get_datas_with_fixture_add_float):
        data = get_datas_with_fixture_add_float
        assert data[2] == data[0] + data[1]

    def test_div(self, get_instance, get_datas_with_fixture_div):
        data = get_datas_with_fixture_div
        assert data[2] == data[0] / data[1]

    def test_div_by_zero(self, get_instance, get_datas_with_fixture_div_by_zero):
        data = get_datas_with_fixture_div_by_zero
        assert data[2] == data[0] / data[1]
