"""
从根目录查找文件
"""
import sys
sys.path.append("..")
"""导入计算器的类"""
from pythoncode.Calculator import Calculator
"""导入获取数据的函数"""
import get_datas_function
import pytest
import yaml

@pytest.fixture()
def get_instance():
    print("开始计算")
    calc:Calculator = Calculator()
    yield calc
    print("结束计算")


# 测试计算器的类
class TestCalc:

    """调用get_datas（）函数获取数据"""
    # datas:list = get_datas_function.get_datas()
    add_int_datas:list = get_datas_function.get_datas("add", "int")
    add_float_datas:list = get_datas_function.get_datas("add", "float")
    div_date_datas:list = get_datas_function.get_datas("div", "int")
    div_zero_datas:list = get_datas_function.get_datas("div","div_by_zero")
    # print(add_int_datas)
    # print(float_int_datas)



    # 定义类开始要做的操作：实例化一个计算器
    def setup_class(self):
        print("开始计算")
        self.cal = Calculator()

    def teardown_class(self):
        print("结束计算")

    # 给加法计算器添加一个search标签
    @pytest.mark.search
    # 参数化，可以实现生成多条测试用例，即便有测试用例失败了，其他测试用例也可以正常执行，而不会中断执行。
    @pytest.mark.parametrize("a,b,result",add_int_datas[0],ids=add_int_datas[1])
    # 测试加法计算器
    def test_add(self, a, b, result):
        print(f"a = {a},b = {b},result = {result}")
        # cal = Calculator()
        assert result == self.cal.add(a, b)
    @pytest.mark.parametrize("a,b,result",add_float_datas[0],ids=add_float_datas[1])
    def test_float_add(self, a, b, result):
        print(f"a = {a},b = {b},result = {result}")
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    # 测试减法计算器
    # 给除法计算器添加一个标签
    @pytest.mark.login
    @pytest.mark.parametrize("a,b,result",div_date_datas[0],ids=div_date_datas[1])
    def test_div(self,a,b,result):
        print(f"a = {a},b = {b},result = {result}")
        # cal = Calculator()
        assert result == self.cal.div(a,b)

    @pytest.mark.parametrize("a,b,result",div_zero_datas[0],ids=div_zero_datas[1])
    def test_div_zero(self,a,b,result):
        print(f"a = {a},b = {b},result = {result}")
        # cal = Calculator()
        with pytest.raises(ZeroDivisionError):
            print(self.cal.div(a, b))
