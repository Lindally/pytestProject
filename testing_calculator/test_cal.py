from pythoncode.Calculator import Calculator


class TestCalc:

    def test_add(self):
        cal = Calculator()
        assert 3 == cal.add(1, 1)

    def test_div(self):
        cal = Calculator()
        assert 2 == cal.div(4, 2)
