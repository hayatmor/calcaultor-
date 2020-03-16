import calculator


class TestCalcualtor:
    def test_add(self):
        assert 4 == calculator.add(2, 2)

    def test_sub(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multi(self):
        assert 100 == calculator.multi(10, 10)
