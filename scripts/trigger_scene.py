# scripts/trigger_button.py
from src.registry.manager import load_registry
from src.homekit.driver import HomeKitButtonServer

registry = load_registry()
buttons = registry.get("homekit_buttons", {})

server = HomeKitButtonServer(buttons_registry=buttons)
server.trigger_button("scene_1", press_type=0)
