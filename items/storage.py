from dataclasses import dataclass, field

from items.item import Item

@dataclass
class Storage:
    items: list[Item] = field(default_factory=list)