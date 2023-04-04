import ccxt
import pytest

from src import get_last_prices


@pytest.mark.parametrize(
    "expected",
    [
        ccxt.binance().fetch_ohlcv('ETH/USDT', '1h', limit=2)
    ])
def test_get_last_prices(expected):
    assert get_last_prices()[0] == expected[0][-2]
