from src.algorithms import filter_even, sum_positive


def test_sum_positive_basic():
    assert sum_positive([1, -2, 3, 0]) == 4

def test_filter_even():
    assert filter_even([1, 2, 3, 4]) == [2, 4]