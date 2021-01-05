"""Showcases how the Binance client works."""

from binance.client import Client

client = Client()

print(client.get_order_book(symbol="ETHBTC"))
