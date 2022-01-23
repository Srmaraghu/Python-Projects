import math
import random
import game


class Player:
    def __init__(self,letter) :
        self.letter=letter #letter is either X or O.
    
    def get_move(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter) :
        super().__init__(letter)
        
    def get_move(self,game):
        pass

class HumanPlayer(Player):
    def __init__(self,letter) :
        super().__init__(letter)
        
    def game_move(self,game):
        pass