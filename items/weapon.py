from dataclasses import dataclass

from item import Item

@dataclass
class Weapon(Item):
    damage: int
    # durability: int