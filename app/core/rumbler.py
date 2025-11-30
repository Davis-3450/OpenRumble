import time

from app.controllers.configs.patterns import Intensity, Pattern, PresetPatterns, Wait
from app.controllers.ps4.core import PS4Controller
from app.controllers.xbox.core import XboxController


class Rumbler:
    def __init__(self, controller: XboxController | PS4Controller):
        self.controller = controller

    def play_pattern(self, pattern: Pattern):
        self._runner(pattern)

    def _runner(self, pattern: Pattern):
        for action in pattern.actions:
            if isinstance(action, Wait):
                time.sleep(action.seconds)
            elif isinstance(action, Intensity):
                self.controller.set_vibration(action.left, action.right)

    def get_presets(self) -> dict[str, Pattern]:
        return {pattern.name: pattern.value for pattern in PresetPatterns}
