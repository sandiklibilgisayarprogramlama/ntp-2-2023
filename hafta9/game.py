from team import Team
from typing import Tuple


class Game:
    def __init__(self, location: str, team_a: Team, team_b: Team, score: Tuple) -> None:
        self.location = location
        self.team_a = team_a
        self.team_b = team_b
        self.score = score
