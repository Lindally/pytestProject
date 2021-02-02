import yaml

"""
函数get_datas()：从calc.yal文件获取测试数据
"""


def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        # print("datas")
        return datas["add"]["data"],datas["add"]["ids"],datas["div"]["data"],datas["div"]["ids"]
