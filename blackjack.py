import re

from deck import Deck, deck_36_cards
from player import Player

# 36 карт
# ходят по очереди
# не вскрываемся 

class BlackJack:
    _deck = deck_36_cards()
    _players: [Player]
    _value_to_points={
        6:6,
        7:7,
        8:8,
        9:9,
        10:10,
        'J':2,
        'Q':3,
        'K':4,
        'A':1,
    } 
    
    def __init__(self):
        self._deck = deck_36_cards()
        self._deck.shuffle()
        self._players = []
        

    def _count_players_score(self, player: Player):
        points_total=0
        for card in player.cards: 
            value=card.value
            points=self._value_to_points[value]
            points_total+= points 
        return points_total

    def _get_yes_no(self):
        no_regexp=" *([нН][еЕ]?[тТ]?)|([nN][oO]?)"
        yes_regexp=" *([дД][аА]?)|([yY][eE]?[sS]?)"
        take_card=None 
        while take_card is None :
            answer = input("Берешь карту? <Да/Нет>")
            if re.match(no_regexp, answer):
                take_card= False 
            elif re.match(yes_regexp, answer):
                take_card=True 
            else:
                print('Неправильный ответ, повторите')
        return take_card




    def add_player(self, player):
        self._players.append(player)

    def play(self):
        #TODO: 2 карты в начале
        for player in self._players:
            player.cards.append(self._deck.pop())
            player.cards.append(self._deck.pop())
        for player in self._players:
            self.player_turn(player)


        best=0,[]
        for player in self._players:
            player_score=self._count_players_score(player)
            if player_score>21:
                player_score=0
            if player_score== best[0]:
                best[1].append(player)
            elif player_score>best[0]:
                best=player_score, [player]
        
        print(f"Победители набрали {best[0]} очков")
        for winner in best[1]:
            print(winner.name)
        


            


            
        
            
    def player_turn(self, player: Player):
        print(f"ПРивет, {player.name}. Ходи.")
        while self._count_players_score(player)<21:
            print(f"Очков: {self._count_players_score(player)} ")
            take_card=self._get_yes_no()
            if take_card:
                card_from_deck=self._deck.pop()
                player.cards.append(card_from_deck)
                print(card_from_deck)
            else:
                break
        if self._count_players_score(player) > 21:            
            print(f"Эх, неудача, {player.name}. Ваш счет {self._count_players_score(player)}")
        else:
            print(f"Хорошая игра, {player.name}. Ваш счет {self._count_players_score(player)}")
            
                  

