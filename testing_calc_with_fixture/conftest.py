import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pythoncode import Calculator
from testing_calculator import get_datas_function as datas

import yaml


@pytest.fixture(scope='class')
def get_instance():
    print("开始计算")
    calc: Calculator = Calculator.Calculator()
    yield calc
    print("结束计算")


@pytest.fixture(params=datas.get_datas("add", "int")[0], ids=datas.get_datas("add", "int")[1])
def get_datas_with_fixture_add_int(request):
    return request.param


@pytest.fixture(params=datas.get_datas("add", "float")[0], ids=datas.get_datas("add", "float")[1])
def get_datas_with_fixture_add_float(request):
    return request.param

@pytest.fixture(params=datas.get_datas("div", "int")[0], ids=datas.get_datas("div", "int")[1])
def get_datas_with_fixture_div(request):
    return request.param

@pytest.fixture(params=datas.get_datas("div", "div_by_zero")[0], ids=datas.get_datas("div", "div_by_zero")[1])
def get_datas_with_fixture_div_by_zero(request):
    return request.param
