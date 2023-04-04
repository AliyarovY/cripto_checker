import pytest

from src.utils import get_difference


@pytest.mark.parametrize(
    "input, expected",
    [
        ([1, 2, 3], None),
        (2, None),
        ([], None),
        ('34, 5 3', None),
        (['3', 44], None),
        ([44], None),
        ([44, 22], -22),
        ([22, 44], 22),
        ([-33, -22], -11),
        ([11, -2], -9),
        ([-2, 11], 9),
        ([-1, -4], 3),
    ])
def test_get_difference(input, expected):
    assert get_difference(input) == expected
