import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(dotenv_path=env_path)

WISER_IP = os.getenv("WISER_IP")
WISER_TOKEN = os.getenv("WISER_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {WISER_TOKEN}",
    "Content-Type": "application/json"
}

def upload_script(scene_name: str) -> str:
    """Uploads the wiser_script.py with the scene_name inserted, using raw upload."""
    from pathlib import Path

    # Load script template and inject scene_name
    script_path = Path(__file__).resolve().parents[1] / "scripts" / "wiser_script.py"
    content = script_path.read_text(encoding="utf-8").replace("{scene_name}", scene_name)

    # Prepare the upload
    script_filename = f"script_{scene_name}.py"
    url = f"http://{WISER_IP}/api/scripts/{script_filename}"

    headers = {
        "Authorization": f"Bearer {WISER_TOKEN}",
        "Content-Type": "text/x-python"
    }

    print(f"📤 Uploading MicroPython script as: {script_filename}")

    response = requests.post(url, headers=headers, data=content)

    if response.status_code == 200:
        print(f"✅ Script uploaded for {scene_name}")
        return script_filename  # return filename to pass to assign_job
    else:
        raise Exception(f"❌ Upload failed: {response.status_code} - {response.text}")

def assign_job(device_id: str, input_channel: int, script_name: str):
    """Assigns the script (by filename) to a SmartButton via /api/jobs."""
    payload = {
        "source": {
            "device_id": device_id,
            "input_channel": input_channel
        },
        "target": {
            "type": "script",
            "script_id": script_name  # Wiser accepts filename as script_id
        }
    }

    print(f"🧷 Assigning job: {device_id} ch{input_channel} → {script_name}")

    response = requests.post(
        f"http://{WISER_IP}/api/jobs",
        headers=HEADERS,
        json=payload
    )

    if response.status_code == 200:
        print(f"✅ Job assigned to {device_id} channel {input_channel}")
    else:
        raise Exception(f"❌ Failed to assign job: {response.status_code} - {response.text}")

