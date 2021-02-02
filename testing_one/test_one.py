# 一个计算器程序
import pytest

def add(a,b):
    return a+b
#
def test_add():
    assert 2 == add(1,1)