from dotenv import load_dotenv
import os

load_dotenv()

WISER_IP = os.getenv("WISER_IP")
WISER_TOKEN = os.getenv("WISER_TOKEN")
