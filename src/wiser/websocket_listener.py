import websocket
import threading
import time
import json
from src.utils.config import WISER_IP, WISER_TOKEN

def on_message(ws, message):
    print("📩 Received message:")
    try:
        data = json.loads(message)
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"⚠️ Could not decode JSON: {e}")
        print(message)

def on_error(ws, error):
    print(f"❌ WebSocket Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"🔌 WebSocket closed: {close_status_code}, {close_msg}")

def on_open(ws):
    print("🔗 WebSocket connection opened")

def start_wiser_websocket():
    print(f"📡 WISER_IP loaded: {WISER_IP}")
    print(f"🔑 WISER_TOKEN loaded: {WISER_TOKEN[:5]}...")

    if not WISER_IP or not WISER_TOKEN:
        print("❌ Missing WISER_IP or WISER_TOKEN in environment!")
        return

    url = f"ws://{WISER_IP}/ws?access_token={WISER_TOKEN}"
    print(f"🚀 Connecting to Wiser WebSocket at {url}")

    ws = websocket.WebSocketApp(url,
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close,
                                 on_open=on_open)

    print("🌀 Starting WebSocket client thread...")
    wst = threading.Thread(target=ws.run_forever)
    wst.daemon = True
    wst.start()

    print("🌀 WebSocket client thread started!")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("👋 WebSocket listener stopped.")

# Make sure the function is called if script is executed
if __name__ == "__main__":
    start_wiser_websocket()
