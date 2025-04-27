import requests
import argparse
import getpass
from pathlib import Path

def save_token_to_env(token):
    env_path = Path(".env")

    # If .env exists, read it
    if env_path.exists():
        lines = env_path.read_text().splitlines()
        new_lines = []
        token_set = False

        for line in lines:
            if line.startswith("WISER_TOKEN="):
                new_lines.append(f"WISER_TOKEN={token}")
                token_set = True
            else:
                new_lines.append(line)

        if not token_set:
            new_lines.append(f"WISER_TOKEN={token}")

        env_path.write_text("\n".join(new_lines) + "\n")
    else:
        # If no .env, create it
        env_path.write_text(f"WISER_TOKEN={token}\n")

    print("\n💾 Token saved to .env successfully!")

def get_token(ip, username, password):
    url = f"http://{ip}/api/account/claim"
    payload = {
        "user": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            access_token = data.get("access_token")
            if access_token:
                print("\n✅ Access Token retrieved successfully:")
                print(access_token)

                save_token_to_env(access_token)
            else:
                print("\n❌ No access_token in response!")
                print(data)
        else:
            print(f"\n❌ Authentication failed: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Authenticate with Feller Wiser API and retrieve access token")
    parser.add_argument("--ip", required=True, help="Wiser device IP or hostname (e.g., wiser-00405107)")
    parser.add_argument("--username", default="installer", help="Username (default: installer)")

    args = parser.parse_args()
    password = getpass.getpass(prompt=f"🔑 Password for {args.username}@{args.ip}: ")

    get_token(args.ip, args.username, password)
