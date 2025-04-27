from pyhap.accessory_driver import AccessoryDriver
from src.homekit.accessories import VirtualSceneButton
from flask import Flask, request, jsonify

class HomeKitButtonServer:
    def __init__(self, buttons_registry, port=51826, api_port=5000):
        self.driver = AccessoryDriver(port=port)
        self.accessories = {}
        self.buttons_registry = buttons_registry
        self.api_port = api_port

        for scene_id, config in buttons_registry.items():
            accessory = VirtualSceneButton(self.driver, config["name"])
            self.accessories[scene_id] = accessory
            self.driver.add_accessory(accessory)

        # Setup Flask app
        self.app = Flask(__name__)
        self.register_routes()

    def trigger_button(self, scene_id, press_type=0):
        button = self.accessories.get(scene_id)
        if button:
            print(f"🔘 Triggering {scene_id}: {press_type}")
            button.trigger(press_type)
        else:
            print(f"⚠️ Scene ID '{scene_id}' not found in registry.")

    def register_routes(self):
        # Discovery root
        @self.app.route("/", methods=["GET"])
        def list_buttons():
            return jsonify({
                "available_buttons": [f"/trigger/{scene_id}" for scene_id in self.buttons_registry.keys()]
            })

        # Individual button triggers
        for scene_id in self.buttons_registry.keys():
            route = f"/trigger/{scene_id}"
            print(f"🛠️ Setting up endpoint: {route}")

            self.app.add_url_rule(route, endpoint=scene_id, view_func=lambda scene_id=scene_id: self.trigger_http(scene_id), methods=["POST"])

    def trigger_http(self, scene_id):
        data = request.get_json(silent=True) or {}
        press_type = data.get("press_type", 0)
        print(f"🌐 HTTP Trigger received for {scene_id} with press_type {press_type}")
        self.trigger_button(scene_id, press_type=int(press_type))
        return {"status": "success", "scene": scene_id, "press_type": press_type}, 200

    def start(self):
        print("🚀 Starting HomeKit server")
        import threading
        flask_thread = threading.Thread(target=self.app.run, kwargs={"host": "0.0.0.0", "port": self.api_port})
        flask_thread.daemon = True
        flask_thread.start()

        self.driver.start()
