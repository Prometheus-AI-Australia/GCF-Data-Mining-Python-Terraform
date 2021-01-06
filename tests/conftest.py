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
            "key": "data/20180409_075612.json",
            "data": json.dumps(
                {
                    "ETHBTC": binance.get_order_book(symbol="ETHBTC"),
                    "LTCBTC": binance.get_order_book(symbol="LTCBTC"),
                }
            ).encode("utf-8"),
        },
    }


@pytest.fixture
def collect_candlesticks_data():
    return {"event": {}, "context": context, "result": {}}  # TODO  # TODO


@pytest.fixture
def context():
    class ContextObject:
        timestamp = "2018-04-09T07:56:12.975Z"

    return ContextObject
