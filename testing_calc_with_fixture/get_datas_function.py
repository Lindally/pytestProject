import yaml

"""
函数get_datas()：从calc.yal文件获取测试数据
"""


def get_datas(name, type="int"):
    with open("./dates/calc.yml") as f:
        all_datas = yaml.safe_load(f)
        return all_datas[name][type]["data"],all_datas[name][type]["ids"]
        # print(all_datas)
        # return datas["add"]["data"],datas["add"]["ids"],datas["div"]["data"],datas["div"]["ids"]



