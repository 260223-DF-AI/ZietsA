import pytest 

def func(x):
        return x + 1

class Test_File:
    def test_answer(self):
        assert func(3) == 4

    def test_sum(self):
        assert (0.19 + 0.29) == pytest.approx(0.48)