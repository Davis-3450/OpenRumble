import ctypes
import threading
from typing import TYPE_CHECKING

from app.controllers.base.core import BaseController
from app.controllers.xbox.windows import XInputRumble
from app.utils.enums import RumbleStatus
from app.utils.exceptions import OperatingSystemNotSupported

if TYPE_CHECKING:
    from ctypes import WinDLL


class XboxController(BaseController):
    """Xbox Controller."""

    def __init__(self, user_index=0):
        self.user_index = user_index
        self._xinput = self._set_xinput()
        super().__init__()

    def _set_xinput(self):
        try:
            lib: WinDLL = ctypes.windll.xinput1_4
        except AttributeError:
            try:
                lib: WinDLL = ctypes.windll.xinput9_1_0
            except AttributeError:
                raise OperatingSystemNotSupported(
                    "XInput library not found. Are you on Windows?"
                )
        return lib

    def stop(self) -> RumbleStatus:
        """Stop the controller."""
        self.stop_event.set()

        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)

        with self.lock:
            self.set_vibration(0, 0)

        self.status = RumbleStatus.STOPPED
        return self.status

    def run_pattern(self, pattern_func) -> RumbleStatus:
        self.stop()

        self.thread = threading.Thread(
            target=pattern_func, args=(self, self.stop_event), daemon=True
        )

        self.thread.start()
        self.status = RumbleStatus.RUNNING
        return self.status

    def set_vibration(self, left: float, right: float):
        """Set the vibration of the controller."""
        rumble_struct: XInputRumble = XInputRumble(
            wLeftMotorSpeed=int(max(0, min(1, left)) * 65535),
            wRightMotorSpeed=int(max(0, min(1, right)) * 65535),
        )
        with self.lock:
            try:
                result = self._xinput.XInputSetState(
                    self.user_index, ctypes.byref(rumble_struct)
                )
                return RumbleStatus.RUNNING if result == 0 else RumbleStatus.STOPPED
            except Exception:
                return RumbleStatus.ERROR

    # def _set_vibration_raw(self, left: float, right: float):

    def __enter__(self) -> "XboxController":
        return self

    def __exit__(self, *_) -> None:
        self.stop()
