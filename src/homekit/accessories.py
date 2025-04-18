from pyhap.accessory import Accessory
from pyhap.const import CATEGORY_PROGRAMMABLE_SWITCH

class VirtualSceneButton(Accessory):
    category = CATEGORY_PROGRAMMABLE_SWITCH

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        service = self.add_preload_service("StatelessProgrammableSwitch")
        self.char_event = service.configure_char("ProgrammableSwitchEvent")

    def trigger(self, press_type=0):
        self.char_event.set_value(press_type)
