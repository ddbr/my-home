from pyhap.accessory_driver import AccessoryDriver
from src.homekit.accessories import VirtualSceneButton

class HomeKitButtonServer:
    def __init__(self, buttons_registry, port=51826):
        self.driver = AccessoryDriver(port=port)
        self.accessories = {}

        for scene_id, config in buttons_registry.items():
            accessory = VirtualSceneButton(self.driver, config["name"])
            self.accessories[scene_id] = accessory
            self.driver.add_accessory(accessory)

    def trigger_button(self, scene_id, press_type=0):
        button = self.accessories.get(scene_id)
        if button:
            print(f"🔘 Triggering {scene_id}: {press_type}")
            button.trigger(press_type)
        else:
            print(f"⚠️ Scene ID '{scene_id}' not found in registry.")

    def start(self):
        print("🚀 Starting HomeKit server")
        self.driver.start()
