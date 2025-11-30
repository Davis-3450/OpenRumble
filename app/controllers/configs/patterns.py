from dataclasses import dataclass
from enum import Enum


class BaseData:
    pass


@dataclass()
class Wait(BaseData):
    seconds: float


@dataclass()
class Intensity(BaseData):
    left: float
    right: float


@dataclass()
class Pattern(BaseData):
    actions: list[Wait | Intensity]


# default patterns
class PresetPatterns(Enum):
    CONSTANT = Pattern(actions=[Wait(seconds=0.1), Intensity(left=0.8, right=0.8)])
    PULSE = Pattern(
        actions=[
            Wait(seconds=0.1),
            Intensity(left=1.0, right=0.0),
            Wait(seconds=0.1),
            Intensity(left=0.0, right=1.0),
            Wait(seconds=0.6),
            Intensity(left=0.0, right=0.0),
        ]
    )

    # WAVE = Pattern(
    #     actions=[
    #         Wait(seconds=0.05),
    #         Intensity(left=(math.sin(t) + 1) / 2, right=(math.sin(t) + 1) / 2),  # type: ignore
    #         Wait(seconds=0.2),
    #     ]
    # )


# CONSTANT = Pattern(actions=[Wait(seconds=0.1), Intensity(left=0.8, right=0.8)])
# PULSE = Pattern(
#     actions=[
#         Wait(seconds=0.1),
#         Intensity(left=1.0, right=0.0),
#         Wait(seconds=0.1),
#         Intensity(left=0.0, right=1.0),
#         Wait(seconds=0.6),
#         Intensity(left=0.0, right=0.0),
#     ]
# )
# WAVE = Pattern(actions=[Wait(seconds=0.05), Intensity(left=math.sin(t) + 1) / 2, Wait(seconds=0.2)])


# def pattern_constant(controller: XboxController | PS4Controller):
#     while controller.is_running():
#         controller.set_vibration(0.8, 0.8)
#         time.sleep(0.1)


# def pattern_pulse(controller: XboxController | PS4Controller):
#     while controller.is_running():
#         # Bum-Bum (Latido)
#         controller.set_vibration(1.0, 0.0)
#         time.sleep(0.1)
#         controller.set_vibration(0.0, 1.0)
#         time.sleep(0.1)
#         controller.set_vibration(0.0, 0.0)
#         time.sleep(0.6)


# def pattern_wave(controller: XboxController | PS4Controller):
#     t = 0
#     while controller.is_running():
#         # Onda senoidal
#         val: float = (math.sin(t) + 1) / 2  # Normalizar a 0-1
#         controller.set_vibration(val, val)
#         time.sleep(0.05)
#         t += 0.2
