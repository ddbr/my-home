import yaml
from pathlib import Path

def load_button_config():
    config_path = Path(__file__).resolve().parents[1] / "config" / "buttons.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
