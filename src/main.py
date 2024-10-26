# src/main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api.auth import get_access_token
from api.orders import place_order, cancel_order, modify_order
from api.market_data import get_orderbook, get_positions

def main():
    access_token = get_access_token()
    symbol = 'BTC-PERPETUAL'

    # Place a test order
    order_response = place_order(access_token, symbol, 'limit', 1, 30000)
    print("Order Response:", order_response)
    order_id = order_response.get("result", {}).get("order_id")

    # Modify the order if successfully placed
    if order_id:
        modified_order_response = modify_order(access_token, order_id, 30500)
        print("Modified Order Response:", modified_order_response)

        # Cancel the order if successfully modified
        cancel_order_response = cancel_order(access_token, order_id)
        print("Cancel Order Response:", cancel_order_response)

    # Fetch orderbook
    orderbook = get_orderbook(symbol)
    print("Orderbook:", orderbook)

    # Get current positions
    positions = get_positions(access_token)
    print("Positions:", positions)

if __name__ == "__main__":
    main()
