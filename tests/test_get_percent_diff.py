import ccxt
import pytest

from src import get_percent_diff


@pytest.mark.parametrize(
    "input, expected",
    [
        ([100, 90], -10),
        ([100, 120], 20),
        ([], None),
        ('afs', None),
        ([100, 100], 0),
    ])
def test_get_percent_diff(input, expected):
    assert get_percent_diff(input) == expected
