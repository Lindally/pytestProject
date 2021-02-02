"""
模块级(setup_module/teardown_module)模块始末，全局的（ 优先级最高）（不在类中）
函数级(setup_function/teardown_function)只对函数用例生效（不在类中）
类级(setup_class/teardown_class)只在类前后运行一次（在类中）
方法级(setup_method/teardown_method)开始于方法始末（在类中）
类里面的(setup/teardown)运行在调用方法前后（在类中）

"""


def setup_module():
    print("资源准备：setup_module")


def teardown_module():
    print("资源准备完毕:teardown_module")

#定义一个函数
def test_case1():
    print("case1")


def setup_function():
    print("函数开始前：setup_function")


def teardown_function():
    print("函数调用完毕：teardown_function")

# 定义一个类
class TestDemo:

    #  执行类 前后分别执行setup_class  teardown_class
    def setup_class(self):
        print("TestDemo setup_class")

    def teardown_class(self):
        print("TestDemo teardown_class")

    # 每个类里面的方法前后分别执行 setup, teardown
    def setup(self):
        print("TestDemo setup")

    def teardown(self):
        print("TestDemo teardown")
    # 定义类中的一个方法
    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")

# def test_a():
#     print("aaa")
#     pass
#
# def setup_function():
#     print("测试前")
#
# def teardown_function():
#     print("测试后")
