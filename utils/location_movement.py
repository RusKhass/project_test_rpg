import json
import os

MAP_FILE_PATH = "./map.json"

def read_location_from_json():
    if os.path.isfile(MAP_FILE_PATH):
        with open(MAP_FILE_PATH, "r") as f:
            map = json.load(f)
            return map
    else:
        raise ValueError("Map file not found")

def show_current_location(map):
    for idx, location in enumerate(map["locations"]):
        print("{}. {}".format(idx + 1, location["title"]))
    
def get_location_by_idx():
    """get location by idx using console"""
    return int(input("Enter location number: ")) - 1

def move(location, idx):
    """move to the next location"""
    return location["locations"][idx]

def location_movement(map, current=None):
    if current is None:
        current = map
    show_current_location(map)
    idx = get_location_by_idx()
    current = move(map, idx)
    show_current_location(current)
    return current