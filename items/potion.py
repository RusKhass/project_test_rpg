from dataclasses import dataclass

from item import Item
from items.effect import Effect

@dataclass
class Potion(Item):
    duration: int
    effects: list[Effect]