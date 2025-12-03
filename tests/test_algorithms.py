from src.algorithms import sum_positive


def test_sum_positive_basic():
    assert sum_positive([1, -2, 3, 0]) == 4