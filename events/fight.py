from dataclasses import dataclass
from actors.enemy import Enemy

from actors.player import Player

@dataclass
class Fight:
    # steps: int
    
    @staticmethod
    def fight_without_steps(player: Player, enemy: Enemy):
        while player.is_alive() and enemy.is_alive():
            player.attack(enemy)
            enemy.attack(player)
    