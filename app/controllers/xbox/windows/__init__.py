from ctypes import c_ushort

from app.controllers.base.c_structs import BaseCStruct


class XInputRumble(BaseCStruct):
    """Struct for XInput rumble."""

    _fields_ = [
        ("wLeftMotorSpeed", c_ushort),
        ("wRightMotorSpeed", c_ushort),
    ]
