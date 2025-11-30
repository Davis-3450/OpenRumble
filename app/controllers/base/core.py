import threading
from abc import ABC, abstractmethod
from typing import Optional

from app.utils.enums import RumbleStatus


class BaseController(ABC):
    def __init__(self):
        """
        Purpose: base state and synchronization primitives
        """
        self._status: RumbleStatus = RumbleStatus.STOPPED
        self.thread: Optional[threading.Thread] = None
        self.stop_event = threading.Event()
        self.lock = threading.Lock()

    @abstractmethod
    def set_vibration(self, left_motor: float, right_motor: float):
        """
        Purpose: set the vibration of the controller
        """
        raise NotImplementedError("set_vibration method not implemented")

    @abstractmethod
    def stop(self) -> RumbleStatus:
        """
        Purpose: stop the controller
        """
        raise NotImplementedError("stop method not implemented")

    @abstractmethod
    def run_pattern(self, pattern_func) -> RumbleStatus:
        """
        Purpose: run a pattern on the controller
        """
        raise NotImplementedError("run_pattern method not implemented")

    @property
    def status(self) -> RumbleStatus:
        """
        Purpose: get the status of the controller
        """
        return self._status

    @status.setter
    def status(self, value: RumbleStatus) -> None:
        self._status = value

    @status.setter
    def status(self, value: RumbleStatus) -> None:
        """
        Purpose: set the status of the controller
        """
        self._status = value
