import requests

WISER_IP = "wiser-00405107"
WISER_TOKEN = "badc2ab1-08d0-45f3-9263-42a2be926d97"

headers = {
    "Authorization": f"Bearer {WISER_TOKEN}",
    "Content-Type": "application/json"
}

# Read the script
with open("scripts/wiser_script.py", "r", encoding="utf-8") as f:
    content = f.read()

response = requests.post(
    f"http://{WISER_IP}/api/scripts/wiser_script.py",
    headers={
        "Authorization": f"Bearer {WISER_TOKEN}",
        "Content-Type": "text/x-python"
    },
    data=content  # ✅ send as raw body
)

print(response.status_code)
print(response.text)
