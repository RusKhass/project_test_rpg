from dataclasses import dataclass

from item import Item

@dataclass
class Armor(Item):
    defense: int
    # durability: int