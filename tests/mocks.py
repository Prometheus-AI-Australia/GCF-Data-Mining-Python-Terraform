from dataclasses import dataclass


class MockConfiguration:
    class DotDict(dict):
        """
        a dictionary that supports dot notation 
        as well as dictionary access notation 
        usage: d = DotDict() or d = DotDict({'val1':'first'})
        set attributes: d.val2 = 'second' or d['val2'] = 'second'
        get attributes: d.val2 or d['val2']
        """

        __getattr__ = dict.__getitem__
        __setattr__ = dict.__setitem__
        __delattr__ = dict.__delitem__

        def __init__(self, dct):
            for key, value in dct.items():
                if hasattr(value, "keys"):
                    value = DotDict(value)
                self[key] = value

    gcp = DotDict({"bucket": "demo-bucket", "prefix": "data"})
    binance = DotDict(
        {
            "tickers": ["ETHBTC", "LTCBTC"],
            "orderbook_prefix": "orderbook",
            "orderbook_limit": 500,
            "kline_prefix": "candlesticks",
            "kline_interval": "15m",
            "kline_limit": 500,
        }
    )
    context_timestamp_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    filename_timestamp_format = "%Y%m%d_%H%M%S"


class BinanceClientMock:
    def __call__(self):
        return self  # Passthrough for lazy initialisation of client

    def get_order_book(self, symbol, limit=5):
        return {
            "lastUpdateId": 2100298448,
            "bids": [
                ["0.03165600", "54.61900000"],
                ["0.03165400", "24.11200000"],
                ["0.03165300", "0.52500000"],
                ["0.03165100", "0.54400000"],
                ["0.03165000", "5.04000000"],
            ],
            "asks": [
                ["0.03165700", "1.61300000"],
                ["0.03166300", "0.51000000"],
                ["0.03166400", "1.69600000"],
                ["0.03166500", "24.00000000"],
                ["0.03166700", "7.62000000"],
            ],
        }

    def get_klines(self, symbol, interval="15m", limit=5):
        return [
            [
                1609893000000,
                "0.03203000",
                "0.03207000",
                "0.03175300",
                "0.03187200",
                "8728.82400000",
                1609894799999,
                "278.60657984",
                7530,
                "4406.81000000",
                "140.68485539",
                "0",
            ],
            [
                1609894800000,
                "0.03187200",
                "0.03194200",
                "0.03177500",
                "0.03185100",
                "6525.50900000",
                1609896599999,
                "207.93944465",
                6033,
                "3396.80600000",
                "108.25178154",
                "0",
            ],
            [
                1609896600000,
                "0.03185000",
                "0.03186000",
                "0.03145900",
                "0.03170200",
                "10074.46400000",
                1609898399999,
                "318.95867584",
                7871,
                "4862.00200000",
                "153.84853435",
                "0",
            ],
            [
                1609898400000,
                "0.03170300",
                "0.03196300",
                "0.03161500",
                "0.03185100",
                "8937.39600000",
                1609900199999,
                "284.07839101",
                6583,
                "4872.99700000",
                "154.83933927",
                "0",
            ],
            [
                1609900200000,
                "0.03185200",
                "0.03188400",
                "0.03171400",
                "0.03177900",
                "3261.85900000",
                1609901999999,
                "103.67949993",
                2689,
                "1321.65300000",
                "42.01807961",
                "0",
            ],
        ]


class GCSClientMock:
    buckets = {}

    def __call__(self):
        return self  # Passthrough for lazy initialisation of client

    def bucket(self, bucket_name):
        bucket = GCSBucketMock(bucket_name)

        print(bucket_name)
        self.buckets[bucket_name] = bucket
        return bucket


class GCSBucketMock:
    blobs = {}

    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def blob(self, blob_name):
        blob = GCSBlobMock(blob_name=blob_name)
        self.blobs[blob_name] = blob
        return blob


class GCSBlobMock:
    def __init__(self, blob_name):
        self.blob_name = blob_name
        self.data = None

    def download_as_string(self):
        return self.data.decode("utf-8")

    def upload_from_string(self, data, content_type="text/plain"):
        self.data = data.encode("utf-8")
        return self

