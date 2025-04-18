from src.registry.manager import load_registry
from src.homekit.driver import HomeKitButtonServer

def main():
    registry = load_registry()
    buttons = registry.get("homekit_buttons", {})

    server = HomeKitButtonServer(buttons_registry=buttons)
    server.start()

if __name__ == "__main__":
    main()
