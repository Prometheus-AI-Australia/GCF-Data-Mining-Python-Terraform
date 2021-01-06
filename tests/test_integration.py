"""Checks for intended I/O and functionality of the function."""

from src.function import main

from mocks import MockConfiguration, BinanceClientMock, GCSClientMock, GCSBlobMock

###########
## Shims ##
###########

main.config = MockConfiguration()
main.binance.configure(main.config)
main.gcs.configure(main.config)

main.binance.client = BinanceClientMock()
main.gcs.client = GCSClientMock()

#######################
## Integration Tests ##
#######################


def test_collect_orderbooks(collect_orderbooks_data):
    event = collect_orderbooks_data["event"]
    context = collect_orderbooks_data["context"]

    response = main.collect_orderbooks(event, context)

    result = collect_orderbooks_data["result"]
    assert result["bucket"] in main.gcs.client.buckets

    bucket = main.gcs.client.buckets[result["bucket"]]
    assert result["key"] in bucket.blobs

    blob = bucket.blobs[result["key"]]
    assert result["data"] == blob.data
