from player import Player
from blackjack import BlackJack

game=BlackJack()
game.add_player(Player("Шарк"))
game.add_player(Player("Артем"))


game.play()