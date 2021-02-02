import yaml
def test_yaml():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        print(datas["add"]["data"])
        print(datas["add"]["ids"])
