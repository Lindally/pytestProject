"""
定义计算器的类
"""

#被测类
class Calculator():
    # 加法计算器
    def add(self, a, b):
        return a + b

    # 除法计算器
    def div(self, a, b):
        try:
            a / b
        except ZeroDivisionError:
            print("You can't divided by 0!")
        else:
            return a / b
