import time

from utils import *


def main(
        window_size: int = 100,
        timeframe: int = 3_600
):
    while True:
        impact = get_price_impact(window_size=window_size)
        for _ in range(window_size):
            prices = get_last_prices()
            if is_valid_diff(impact, prices):
                print('Big changes !')
            time.sleep(timeframe)


if __name__ == '__main__':
    main()
