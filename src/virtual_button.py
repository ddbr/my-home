from pyhap.accessory import Accessory
from pyhap.accessory_driver import AccessoryDriver
from pyhap.const import CATEGORY_PROGRAMMABLE_SWITCH
import logging
import threading

logging.basicConfig(level=logging.INFO)

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

        # Required for buttons to be accepted by HomeKit
        self.button_service.configure_char('ServiceLabelNamespace', value=1)  # 1 = Alphabetical
        self.button_service.configure_char('ServiceLabelIndex', value=1)      # Index = 1

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
            logging.info(f"🔘 Simulating button press: {press_type}")
            self.char_event.set_value(press_type)
