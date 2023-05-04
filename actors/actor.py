from dataclasses import dataclass

from items.item import Item
from items.storage import Storage

@dataclass
class Actor:
    """Actor is an abstract class"""
    first_name: str
    hp: int
    inventory: Storage
    
    # def __init__(self):
    #     raise NotImplementedError("Actor is an abstract class")