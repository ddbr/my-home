Here you go — clean and ready for **copy-paste** into your `README.md` file:

# 🏡 My Home — HomeKit + Feller Wiser Integration

This project integrates HomeKit virtual buttons with Feller Wiser scenes.  
You can trigger HomeKit devices based on Wiser button scenes and automate your smart home with flexible mappings.

---

## 🚀 Quick Setup

```bash
git clone https://github.com/ddbr/my-home.git
cd my-home
bash setup.sh
source .venv/bin/activate
python -m src.main
```

✅ This starts the HomeKit server and exposes a Flask HTTP API for button triggers.

---

## 📚 Project Structure

```
my-home/
├── config/             # HomeKit button registry (registry.yaml)
├── scripts/            # (optional) test scripts
├── src/
│   ├── homekit/        # HAP-python server and virtual accessories
│   ├── registry/       # Loads HomeKit button registry
│   ├── utils/          # Config loader (dotenv)
│   └── main.py         # Entry point: starts server and Flask API
├── .env                # Local environment settings
├── requirements.txt    # Python dependencies
├── setup.sh            # Easy local setup script
└── README.md           # This file
```

---

## 🔘 How to Trigger a HomeKit Button via HTTP

Once your server is running, you can trigger your HomeKit buttons through a simple HTTP POST call.

### Example (Single Press):

```bash
curl -X POST http://localhost:5000/trigger/scene_1
```

✅ This simulates a **single press** (`press_type = 0`) on the button registered as `scene_1`.

---

### Example (Double Press):

```bash
curl -X POST http://localhost:5000/trigger/scene_1 \
  -H "Content-Type: application/json" \
  -d '{"press_type": 1}'
```

- `press_type` values:
  - `0` = Single Press
  - `1` = Double Press
  - `2` = Long Press

---

### 🚀 Discover Available Endpoints

When you open [http://localhost:5000/](http://localhost:5000/) in your browser,  
the server shows a list of all available `/trigger/{scene_id}` endpoints dynamically based on your `registry.yaml`.

Example JSON output:

```json
{
  "available_buttons": [
    "/trigger/scene_1",
    "/trigger/scene_2"
  ]
}
```

---

## 🌟 Coming Next

- Feller Wiser scene listener integration
- Dynamic HomeKit device registration (no restart needed)
- Real-time LED feedback updates to Wiser buttons
- Web UI for mapping buttons to actions

---

## 🛡 Requirements

- Python 3.9+
- Raspberry Pi 4 (or any Linux/Mac/PC environment)
- iOS Device (for HomeKit testing)

---

## ✨ Notes

- Stateless switches are used by default to allow HomeKit Automations flexibility.
- The integration is designed to be extendable towards MQTT, Home Assistant, and external Webhooks.

