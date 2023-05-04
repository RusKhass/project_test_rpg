import json
from actors.enemy import Enemy
from actors.player import Player
from events.fight import Fight
from items.storage import Storage
from locations.location import Location
from utils.game_exeptions import ExitGame
from utils.location_movement import location_movement, read_location_from_json, show_current_location
from utils.map_maker import map_maker

def runGame(map):
    current = map
    while True:
        current = location_movement(map, current)

# while player.is_alive():
#     for enemy in enemies:
#         Fight.fight_without_steps(player, enemy)
#         if not player.is_alive():
#             break

# if player.is_alive():
#     print("You won!")
# else:
#     print("Wasted!")

map = read_location_from_json()

try:
    runGame(map)
except ExitGame:
    print("Goodbye!")

# current = location_movement(map)
# print('-------------------')
# current = location_movement(current)
# show_current_location(current)


# map_maker()