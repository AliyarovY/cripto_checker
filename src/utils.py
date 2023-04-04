import ccxt


def get_last_prices(symbol='ETH/USDT', timeframe='1h', window_size=2, exchange=ccxt.binance()) -> list[int]:
    try:
        prices = exchange.fetch_ohlcv(symbol, timeframe, limit=window_size)
    except Exception as e:
        print(e)
    else:
        return [x[-2] for x in prices]


def get_difference(prices: list[int]) -> int | None:
    if not hasattr(prices, '__iter__'):
        return None

    args_check = (
        isinstance(prices, str),
        len(prices) != 2,
        any(not isinstance(x, (int, float)) for x in prices),
    )

    if any(args_check):
        return None

    prices = [abs(x) for x in prices]
    previous_price, current_price = prices
    return current_price - previous_price


def get_percent_diff(prices: list[int]) -> int | None:
    diff = get_difference(prices)
    if diff is None:
        return None
    previous_price = prices[0]
    res = diff / (previous_price / 100)
    return int(res)


def is_valid_diff(impact: int, prices: list[int], percent: int = 1) -> bool | None:
    if percent not in range(1, 101):
        return None

    percent_diff = get_percent_diff(prices)
    leader_price_diff = get_percent_diff(get_last_prices(symbol='BTC/USDT'))

    if None in (percent_diff, leader_price_diff):
        return None

    impact = leader_price_diff * impact
    result = abs(percent_diff - impact) >= percent
    return result


def get_price_impact(
        window_size: int = 100,
        exchange: ccxt = ccxt.binance(),
        leader_symbol: str = 'BTC/USDT',
        slave_symbol: str = 'ETH/USDT',
        timeframe: str = '1h',
) -> int:
    # create prices lists
    leader_prices = exchange.fetch_ohlcv(leader_symbol, timeframe, limit=window_size)
    slave_prices = exchange.fetch_ohlcv(slave_symbol, timeframe, limit=window_size)

    # collecting impact in percent
    sum_impacts = 0
    for i in range(1, window_size):
        leader_vector = get_percent_diff([leader_prices[i - 1], leader_prices[i]])
        slave_vector = get_percent_diff([slave_prices[i - 1], slave_prices[i]])

        impact = 0

        if not any(x == 0 for x in [leader_vector, slave_vector]):
            impact = slave_vector / leader_vector

        sum_impacts += impact

    # calculate average impact
    result = sum_impacts / (window_size - 1)

    return result
