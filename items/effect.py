from dataclasses import dataclass
import enum

class EffectType(enum.Enum):
    HEAL = enum.auto()
    DAMAGE = enum.auto()


@dataclass
class Effect:
    type: str
    points: int