import json
import os
from utils.game_exeptions import ExitGame

from utils.map_maker import search_location_in_dict

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
    print("-1. back")
    print("q. exit")
    
def get_location_by_idx():
    """get location by idx using console"""
    return input("Enter location number: ")

def move(location, idx):
    """move to the next location"""
    return location["locations"][idx]

def location_movement(map, current):
    show_current_location(current)
    idx = get_location_by_idx()
    if idx == '-1':
        current = search_location_in_dict(map, current["previous_location"])
    elif idx.isnumeric():
        idx = int(idx) - 1
        try:
            current = move(current, idx)
        except IndexError:
            print("Wrong location number")
    elif idx == 'q':
        raise ExitGame
    return current