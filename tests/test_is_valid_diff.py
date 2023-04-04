import pytest

from src import is_valid_diff


@pytest.mark.parametrize(
    "input",
    [
        ([], 2),
        ([3], 1),
        (['4', 4], 1),
        ([11, 11], '0'),
        ([11, 22], 444),
        (44, 9),
    ])
def test_is_valid_diff_None(input):
    assert is_valid_diff(*input) == None


@pytest.mark.parametrize(
    "input",
    [
        ([100, 4], 1),
        ([100, 1], 1),
        ([100, 50], 1),
        ([100, 99], 1),
        ([200, 186], 5),
    ])
def test_is_valid_diff_correct(input):
    assert is_valid_diff(*input) == True
