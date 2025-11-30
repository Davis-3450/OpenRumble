import threading
import time
from itertools import cycle
from typing import Optional

from app.controllers.configs.patterns import Intensity, Pattern, PresetPatterns, Wait
from app.controllers.ps4.core import PS4Controller
from app.controllers.xbox.core import XboxController
from app.utils.enums import RumbleStatus


class Rumbler:
    def __init__(self, controller: XboxController | PS4Controller):
        self.controller = controller
        self._status: RumbleStatus = RumbleStatus.STOPPED
        self._thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()

    @property
    def status(self) -> RumbleStatus:
        return self._status

    def play_pattern(self, pattern: Pattern) -> RumbleStatus:
        self.stop()
        self._stop_event.clear()
        self._thread = threading.Thread(
            target=self._runner, args=(pattern,), daemon=True
        )
        self._thread.start()
        self._status = RumbleStatus.RUNNING
        return self._status

    def stop(self) -> RumbleStatus:
        self._stop_event.set()
        if self._thread and self._thread.is_alive():
            self._thread.join(timeout=1.0)
        # Ensure motors are off
        try:
            self.controller.set_vibration(0.0, 0.0)
        finally:
            self._status = RumbleStatus.STOPPED
        return self._status

    def _wait_with_cancel(self, seconds: float) -> None:
        remaining = max(0.0, seconds)
        step = 0.02
        while remaining > 0 and not self._stop_event.is_set():
            sleep_time = min(step, remaining)
            time.sleep(sleep_time)
            remaining -= sleep_time

    def _runner(self, pattern: Pattern) -> None:
        for action in cycle(pattern.actions):
            if self._stop_event.is_set():
                break
            if isinstance(action, Wait):
                self._wait_with_cancel(action.seconds)
            elif isinstance(action, Intensity):
                self.controller.set_vibration(action.left, action.right)
        # turn off on exit
        self.controller.set_vibration(0.0, 0.0)
        self._status = RumbleStatus.STOPPED

    def get_presets(self) -> dict[str, Pattern]:
        return {pattern.name: pattern.value for pattern in PresetPatterns}
