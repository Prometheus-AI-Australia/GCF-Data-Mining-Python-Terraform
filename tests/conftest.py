import os
import json

import pytest

from mocks import BinanceClientMock


@pytest.fixture
def collect_orderbooks_data(context):
    binance = BinanceClientMock()

    return {
        "event": {},  # TODO
        "context": context,
        "result": {
            "bucket": "demo-bucket",
            "key": "data/orderbook/20180409_075612.json",
            "data": json.dumps(
                {
                    "ETHBTC": binance.get_order_book(symbol="ETHBTC"),
                    "LTCBTC": binance.get_order_book(symbol="LTCBTC"),
                }
            ),
        },
    }


@pytest.fixture
def collect_candlesticks_data(context):
    binance = BinanceClientMock()

    return {
        "event": {},  # TODO
        "context": context,
        "result": {
            "bucket": "demo-bucket",
            "key": "data/candlesticks/20180409_075612.json",
            "data": json.dumps(
                {
                    "ETHBTC": binance.get_klines(symbol="ETHBTC"),
                    "LTCBTC": binance.get_klines(symbol="LTCBTC"),
                }
            ),
        },
    }


@pytest.fixture
def context():
    class ContextObject:
        timestamp = "2018-04-09T07:56:12.975Z"

    return ContextObject
