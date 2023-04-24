from team import Team
from game import Game
from typing import List


class SoccerLeague:
    def __init__(self, teams: List[Team], games: List[Game]) -> None:
        self.teams = teams
        self.games = games

    def get_team(self, name: str) -> Team:
        for team in self.teams:
            if name == team.name:
                return team

    def get_game(self, team_a: Team, team_b: Team) -> Game:
        for game in self.games:
            if game.team_a == team_a and game.team_b == team_b:
                return game

    def print_teams(self) -> None:
        print("---Teams")
        for team in self.teams:
            print(team.name)

    def print_games(self) -> None:
        print("---Games")
        for game in self.games:
            print(game.team_a.name, ":", game.team_b.name, " ", game.score)
