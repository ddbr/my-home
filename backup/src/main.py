from src.config_loader import load_button_config
from src import wiser_api
from src.flask_server import start_flask_server
import threading

def main():
    print("🚀 Starting SmartButton deployment...")

    config = load_button_config()
    buttons = config.get("buttons", [])

    for button in buttons:
        device_id = button["device_id"]
        input_channel = button["input_channel"]
        scene_name = button["scene_name"]

        # Upload script with scene_name inserted
        script_id = wiser_api.upload_script(scene_name)

        # Assign script to smart button
        wiser_api.assign_job(device_id, input_channel, script_id)

    # Start Flask trigger server
    threading.Thread(target=start_flask_server, daemon=True).start()
    print("🌐 Flask server started and waiting for Wiser button triggers")

    # Keep main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("👋 Server shutdown requested")

if __name__ == "__main__":
    main()
