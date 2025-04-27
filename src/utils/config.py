import os
from dotenv import load_dotenv
from pathlib import Path

# Force load .env from project root
env_path = Path(__file__).resolve().parents[2] / '.env'
print(f"🌍 Loading .env from: {env_path}")

load_dotenv(dotenv_path=env_path)

WISER_IP = os.getenv("WISER_IP")
WISER_TOKEN = os.getenv("WISER_TOKEN")

print(f"📡 Loaded WISER_IP = {WISER_IP}")
print(f"🔑 Loaded WISER_TOKEN = {WISER_TOKEN[:5]}...")
