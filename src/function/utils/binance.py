from binance.client import Client

from .base import LazyClient


class BinanceClient(LazyClient):
    """Wrapper around raw Binance client."""

    _kline_cols = [
        "openTime",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "closeTime",
        "quoteAssetVolume",
        "numberOfTrades",
        "takerBuyBaseAssetVolume",
        "takerBuyQuoteAssetVolume",
        "NA",
    ]

    def __init__(self, configuration=None):
        super().__init__()
        self.client = Client()

        # Initialise defaults.
        self.tickers = []
        self.orderbook_limit = 500
        self.kline_interval = "15m"
        self.kline_limit = 500

        # Configure if passed in.
        if configuration is not None:
            self.configure(configuration)

    def configure(self, config):
        self.tickers = config.binance.tickers

        self.orderbook_limit = config.binance.orderbook_limit

        self.kline_interval = config.binance.kline_interval
        self.kline_limit = config.binance.kline_limit

        return self

    def get_candlesticks(self):
        data = {}

        for ticker in self.tickers:
            klines = self.client.get_klines(
                symbol=ticker, interval=self.kline_interval, limit=self.kline_limit
            )

            rows = [
                dict(zip(self._kline_cols, data)) for data in klines
            ]  # Converts from unlablelled matrix to labelled rows

            data[ticker] = rows

        return data

    def get_orderbooks(self):
        data = {}

        for ticker in self.tickers:
            orderbook = self.client.get_order_book(
                symbol=ticker, limit=self.orderbook_limit
            )
            data[ticker] = orderbook

        return data

