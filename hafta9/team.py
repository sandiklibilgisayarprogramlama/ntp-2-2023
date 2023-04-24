from coach import Coach
from player import Player
from record import Record
from typing import List


class Team:
    def __init__(self, name: str, record: Record, player_list: List[Player], captain: Player, coach: Coach) -> None:
        self.record = record
        self.player_list = player_list
        self.captain = captain
        self.coach = coach
        self.name = name
