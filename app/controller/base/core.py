from abc import ABC, abstractmethod


class BaseController(ABC):
    def __init__(self, value: int):
        """
        Purpose: value
        """

    @abstractmethod
    def set_vibration(self, left_motor: float, right_motor: float):
        """
        Purpose: set the vibration of the controller
        """
        pass

    @abstractmethod
    def stop(self):
        """
        Purpose: stop the controller
        """
        pass

    @abstractmethod
    def run_pattern(self, pattern_func):
        """
        Purpose: run a pattern on the controller
        """
        pass

    @abstractmethod
    def is_running(self):
        """
        Purpose: check if the controller is running
        """
        pass
