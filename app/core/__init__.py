from app.controllers.ps4.core import PS4Controller
from app.controllers.xbox.core import XboxController
from app.core.rumbler import Rumbler

# TODO:
# - [ ] Add a button to stop | start the pattern
# - [ ] Intensity slider
# - [ ] Pattern selector


class VibeApp:
    def __init__(self):
        self.controller = self._set_controller()
        self.rumble = Rumbler(self.controller)

    def _set_controller(self) -> XboxController | PS4Controller:
        # TODO: implement support for PS4 controllers and selector menu (default: xinput)
        return XboxController()
