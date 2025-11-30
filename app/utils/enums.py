from enum import Enum


class BaseEnum(str, Enum):
    """Base enum."""


class OperatingSystem(BaseEnum):
    """OS Enum"""

    WINDOWS = "windows"
    MACOS = "macos"
    LINUX = "linux"


class ControllerName(BaseEnum):
    """Controller Enum"""

    XBOX = "xbox"
    PS4 = "ps4"


class RumbleStatus(BaseEnum):
    """Status Enum"""

    RUNNING = "running"
    STOPPED = "stopped"
    ERROR = "error"
