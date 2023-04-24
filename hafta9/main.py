from player import Player
from coach import Coach
from game import Game
from team import Team
from position import POSITION
from accr_level import ACCRLEVEL
from record import Record
from soccer_league import SoccerLeague

player1 = Player("Ahmet", "afyon", 1, POSITION.GK)
player2 = Player("ismet", "afyon", 5, POSITION.SW)
player3 = Player("yusuf", "afyon", 10, POSITION.CF)
coach1 = Coach("Okan", "", ACCRLEVEL.HIGH, 10)
record1 = Record(30, 1, 3)

player4 = Player("Necip", "afyon", 1, POSITION.GK)
player5 = Player("Ümit", "afyon", 5, POSITION.SW)
player6 = Player("Recep", "afyon", 10, POSITION.CF)
coach2 = Coach("Mustafa", "", ACCRLEVEL.HIGH, 16)
record2 = Record(28, 3, 3)

team1 = Team("Fenerbahçe", record1, [
             player1, player2, player3], player1, coach1)

team2 = Team("Barcelona", record2, [
             player4, player5, player6], player5, coach2)

game1 = Game("İstanbul", team1, team2, (5, 3))
game2 = Game("Barcelona", team1, team2, (3, 2))

league = SoccerLeague([team1, team2], [game1, game2])

league.print_games()

league.print_teams()
