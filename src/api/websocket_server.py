# src/api/websocket_server.py
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import asyncio
import websockets
import json
from market_data import get_orderbook

SUBSCRIBED_CLIENTS = {}

async def subscribe_symbol(websocket, path):
    async for message in websocket:
        data = json.loads(message)
        action = data.get('action')
        symbol = data.get('symbol')

        if action == 'subscribe':
            if symbol not in SUBSCRIBED_CLIENTS:
                SUBSCRIBED_CLIENTS[symbol] = []
            SUBSCRIBED_CLIENTS[symbol].append(websocket)
            await websocket.send(f"Subscribed to {symbol}")

        while True:
            orderbook = get_orderbook(symbol)
            await websocket.send(json.dumps(orderbook))
            await asyncio.sleep(1)

start_server = websockets.serve(subscribe_symbol, "localhost", 6789)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
