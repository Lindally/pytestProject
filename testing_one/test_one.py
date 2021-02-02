# 一个计算器程序
import pytest

def add(a,b):
    return a+b
#
def test_add(login):
    assert 2 == add(1,1)


def test_add1(login):
    print("我喜欢你！")