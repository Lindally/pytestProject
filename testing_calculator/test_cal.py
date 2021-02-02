import sys

# print(sys.path)
sys.path.append("..")

from pythoncode.Calculator import Calculator
import pytest
import yaml


# 测试类
class TestCalc:

    # 定义类开始要做的操作：实例化一个计算器
    def setup_class(self):
        print("开始计算")
        self.cal = Calculator()

    def teardown_class(self):
        print("结束计算")

    # 测试加法计算器
    # 给加法计算器添加一个标签
    @pytest.mark.search
    # 参数化，可以实现生成多条测试用例，即便有测试用例失败了，其他测试用例也可以正常执行，而不会中断执行。
    @pytest.mark.parametrize("a,b,result",[
        [1,1,2],[100,200,300],[3,4,8],[200,200,400]
    ])
    #获取yaml文件的数值
    def get_datas(self):
        with open("./datas/calc.yml") as f:
            self.datas = yaml.safe_load(f)
            print("datas")
            return self.datas




    def test_add(self,a,b,result):
        print(f"a = {a},b = {b},result = {result}")
        # cal = Calculator()
        assert result == self.cal.add(a,b)

    # 测试减法计算器
    # 给除法计算器添加一个标签
    @pytest.mark.login
    def test_div(self):
        # cal = Calculator()
        assert 2 == self.cal.div(4, 2)
