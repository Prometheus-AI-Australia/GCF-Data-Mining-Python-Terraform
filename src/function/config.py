import os


class GCPConfig:
    bucket = os.environ.get("BUCKET_NAME") or ""
    prefix = os.environ.get("KEY_PREFIX", "").strip("/")


class BinanceConfig:
    tickers = os.environ.get("TICKERS", "").split(",")

    orderbook_limit = int(os.environ.get("ORDERBOOK_LIMIT", 500))

    kline_interval = os.environ.get("KLINE_INTERVAL") or "15m"
    kline_limit = int(os.environ.get("KLINE_LIMIT", 500))


class Configuration:
    gcp = GCPConfig()
    binance = BinanceConfig()

    context_timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    filename_timestamp_format = "%Y%m%d_%H%M%S"
