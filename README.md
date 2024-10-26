Deribit Order Management System
This project is an order execution and management system that allows trading on the Deribit Test environment. It provides basic functionalities to place, cancel, and modify orders and to retrieve orderbook and current positions. The project also includes an optional WebSocket server for live orderbook updates.

Features
Place, cancel, and modify orders on the Deribit Test exchange
Retrieve orderbook data and view current positions
Supports trading for spot, futures, and options on all supported symbols
WebSocket server for real-time orderbook updates for subscribed symbols
Technologies Used
Python: Primary programming language
Requests: For HTTP API calls
Websockets: For WebSocket server implementation
WebSocket King: Tool to test WebSocket connections and interactions

Setup Instructions
Clone the repository: 
git clone https://github.com/pritamjr/order-execution-and-management-system-to-trade
cd deribit_order_system

Install the required packages using pip:
pip install requests websockets


Configure API keys:

Create a Deribit Test account here and generate API keys. Update config/settings.py with your client_id, client_secret, and API URL.

API_URL = "https://test.deribit.com/api/v2"
CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

Run the application:

To start the main functions, run:

python src/main.py

main.py will authenticate, place a sample order, retrieve the orderbook, and view current positions.

Run the WebSocket server (Optional):

The WebSocket server sends live orderbook updates to subscribed clients.

python src/api/websocket_server.py


WebSocket URL: ws://localhost:6789

To subscribe to a symbol, send a JSON message like:

{"action": "subscribe", "symbol": "BTC-PERPETUAL"}


Testing with WebSocket King
Connect to WebSocket server: ws://localhost:6789.
Send and receive data:
Authentication: Authenticate via Deribit WebSocket API before accessing private actions.
Test Subscription: Send {"action": "subscribe", "symbol": "BTC-PERPETUAL"} to receive live updates.

