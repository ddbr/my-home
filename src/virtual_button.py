from pyhap.accessory import Accessory
from pyhap.accessory_driver import AccessoryDriver
from pyhap.const import CATEGORY_PROGRAMMABLE_SWITCH
import threading
import logging

logging.basicConfig(level=logging.INFO)

class VirtualButton(Accessory):
    """A generic HomeKit button for triggering HomeKit automations."""

    category = CATEGORY_PROGRAMMABLE_SWITCH

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Add a stateless programmable switch service with required characteristics
        self.button_service = self.add_preload_service(
            'StatelessProgrammableSwitch',
            chars=['ProgrammableSwitchEvent', 'ServiceLabelIndex', 'ServiceLabelNamespace']
        )

        self.char_event = self.button_service.get_characteristic('ProgrammableSwitchEvent')
        self._lock = threading.Lock()

    def trigger_button(self, press_type=0):
        """
        Triggers a virtual HomeKit button press.
        press_type:
            0 = Single Press
            1 = Double Press
            2 = Long Press
        """
        with self._lock:
            logging.info(f"🔘 Simulating button event: {press_type}")
            self.char_event.set_value(press_type)


def main():
    driver = AccessoryDriver(port=51826, persist_file='virtual_button.state')
    accessory = VirtualButton(driver, 'Virtual Button')

    # Store reference to the accessory so we can trigger from outside (e.g., via Flask)
    driver.accessory = accessory

    driver.start()


if __name__ == '__main__':
    main()
