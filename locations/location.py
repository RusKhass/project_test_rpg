from dataclasses import dataclass, field

from items.storage import Storage


@dataclass
class Location:
    title: str = "Root"
    previous_location: str = "Root"
    locations: list = field(default_factory=list)
    loot: Storage = field(default_factory=Storage)
    
    def to_dict(self):
        return {
            "title": self.title,
            "locations": [location.__dict__ for location in self.locations],
            "previous_location": self.previous_location,
            "loot": self.loot.__dict__
        }