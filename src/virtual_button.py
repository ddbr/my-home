import logging
import threading
from pyhap.accessory import Accessory
from pyhap.accessory_driver import AccessoryDriver
from pyhap.const import CATEGORY_PROGRAMMABLE_SWITCH

logging.basicConfig(level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)  # Optional: set to DEBUG for verbose output

class VirtualButton(Accessory):
    category = CATEGORY_PROGRAMMABLE_SWITCH

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.button_service = self.add_preload_service(
            'StatelessProgrammableSwitch',
            chars=[
                'ProgrammableSwitchEvent',
                'ServiceLabelIndex',
                'ServiceLabelNamespace'
            ]
        )

        # Required config to avoid "not compatible" error
        self.button_service.configure_char('ServiceLabelNamespace', value=1)  # 1 = Alphabetical
        self.button_service.configure_char('ServiceLabelIndex', value=1)      # First button

        self.char_event = self.button_service.get_characteristic('ProgrammableSwitchEvent')
        self._lock = threading.Lock()

    def trigger_button(self, press_type=0):
        """
        Triggers a HomeKit button press.
        0 = Single Press, 1 = Double Press, 2 = Long Press
        """
        with self._lock:
            logging.info(f"🔘 Triggering HomeKit button event: {press_type}")
            self.char_event.set_value(press_type)


def main():
    driver = AccessoryDriver(
        port=51826,
        persist_file='virtual_button.state',
        address='192.168.1.26'  # ⚠️ Set this to your Pi’s actual IP (or leave as None to auto-select)
    )

    accessory = VirtualButton(driver, 'Virtual Button')
    driver.add_accessory(accessory)

    # Optional: expose it for external access (e.g. via Flask later)
    driver.accessory = accessory

    logging.info("🚀 Starting HomeKit accessory 'Virtual Button'")
    driver.start()

if __name__ == '__main__':
    main()
