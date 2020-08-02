import time
from collections import defaultdict

from deuces.deuces import Deck, Card, Evaluator


class player(object):
    def __init__(self, name=None, fortune=100):
        self.name = name if name else "player"+int(time.time())
        self.fortune = fortune
        # Round Info
        self.cards = None
        # Choice made during each phase (preflop, flop, turn, river)
        # 0: check -1:fold (0,+inf):raise
        self.choice = defaultdict(int)
        self.button = False
