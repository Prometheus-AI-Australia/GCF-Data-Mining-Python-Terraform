"""Showcases how the Binance client works."""

from binance.client import Client

client = Client()

print("== ORDER BOOK ==")
print(client.get_order_book(symbol="ETHBTC", limit=5))
print("\n")

print("== CANDLESTICKS ==")
print(
    client.get_klines(symbol="ETHBTC", limit=5, interval=Client.KLINE_INTERVAL_30MINUTE)
)
