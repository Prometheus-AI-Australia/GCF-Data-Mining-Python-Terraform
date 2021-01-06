import sys
import os

sys.path.append(
    os.path.abspath(os.path.split(__file__)[0])
)  # Lets import statements to work during both testing and deployment.

import json
from datetime import datetime

from utils.binance import BinanceClient
from utils.gcs import GCSBucket
from config import Configuration

config = Configuration()
binance = BinanceClient(configuration=config)
gcs = GCSBucket(configuration=config)

#############
## Methods ##
#############


@binance.lazy_init
@gcs.lazy_init
def collect_orderbooks(event, context):
    book = binance.get_orderbooks()

    gcs.upload(
        key=f"{config.gcp.prefix}/{format_filename(context.timestamp)}",
        data=json.dumps(book),
        content_type="application/json",
    )

    return {}


@binance.lazy_init
@gcs.lazy_init
def collect_candlesticks(event, context):
    return {}


###############
## Utilities ##
###############


def format_filename(iso_timestamp, ext=".json"):
    timestamp = datetime.strptime(iso_timestamp, config.context_timestamp_format)

    fname = timestamp.strftime(config.filename_timestamp_format) + ext

    return fname
