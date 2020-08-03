import time
from collections import defaultdict

from libs.deuces.deuces import Deck, Card, Evaluator
 
bb = 1

class ActionError(Exception):
    def __init__(self, action, elab = None):
        self.action = action
        self.elab = elab if elab  else "No elaboration"
    def __str__(self):
        return "Action [{}] Invalid. Detail: {}".format(self.action, self.elab)

class player(object):
    def __init__(self, name=None, fortune=100):
        self.name = name if name else "player"+int(time.time())
        self.fortune = fortune
        self.table = None
        # 0: normal 1:small blind 2: big blind
        self.seat = 0
        self.hands = None

    def get_two(self, cards):
        if not self.table:
            raise ActionError("GET_TWO", "not even seated")
        self.hands = cards

    def check(self):
        pass

    def call(self):
        pass

    def fold(self):
        pass

    def raise(self, amount):
        pass

class game(object):
    def __init__(self, NumPlayers=6, bb=1):
        self.numPlayers = NumPlayers
        # -1 not started; 0 
        self.cur_phase = -1
