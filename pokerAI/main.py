import time

from collections import defaultdict, Iterator

from libs.deuces.deuces import Deck, Card, Evaluator

bb = 1


class ActionError(Exception):
    def __init__(self, action, elab=None):
        self.action = action
        self.elab = elab if elab else "No elaboration"

    def __str__(self):
        return "Action [{}] Invalid. Detail: {}".format(self.action, self.elab)


class player(object):
    def __init__(self, name=None, fortune=100):
        self.name = name if name else "player"+int(time.time())
        self.fortune = fortune
        # 0: normal 1:small blind 2: big blind
        self.hands = None

    def get_two(self, cards):
        self.hands = cards

    def Check(self):
        pass

    def Call(self):
        pass

    def Fold(self):
        pass

    def Raise(self, amount):
        pass


class playerIterator(Iterator):
    """
    @parameter
    seat:       list of items
    button:     index of card dealer
    @output
    player:     player object
    blind:      0:normal 1:small blind 2:bigblind
    stopFlag:   True/False round over 
    """

    def __init__(self, seat, button):
        self.iter_list = seat
        self.button = button
        self.bigBlind = button-1 if button - \
            1 > 0 else button-1+len(self.iter_list)
        self.smallBlind = button-2 if button - \
            2 > 0 else button-2+len(self.iter_list)
        self.cur = self.smallBlind
        self.step = 1

    def __next__(self):
        player = self.iter_list[self.cur]

        blind = 0
        if self.cur == self.bigBlind:
            blind = 2
        if self.cur == self.smallBlind:
            blind = 1

        stopFlag = False
        if self.step % len(self.iter_list) == 0:
            stopFlag = True
        self.step += 1

        self.cur = self.cur+len(self.iter_list) - \
            1 if not self.cur else self.cur-1
        return player, blind, stopFlag


class Table(object):
    def __init__(self, NumPlayers=6, bb=1, debug=0):
        self.numPlayers = NumPlayers
        # -1 not started; 0
        self.cur_phase = -1
        self.seat = []
        self.gameLog = []
        # Clockwise 0, 5, 4, 3, 2, 1
        self.button = 0
        # Debug mode
        self.debug = debug

    def addPlayer(self, Player):
        if len(self.seat) >= 6:
            raise ActionError("addPlayer", "No available seats.")
        self.seat.append(Player)

    def InitGame(self, debug):
        if not debug:
            debug = self.debug
        playerItr = playerIterator(self.seat, self.button)
        deck = Deck()
        # Deal cards
        while 1:
            player, blind, stopFlag = next(playerItr)
            cards = deck.draw(2)
            player.get_two(cards)
            if debug:
                print("For player {}, the current hands are:".format(player.name))
                Card.print_pretty_cards(player.hands)
            if stopFlag:
                break
        # Preflop
        # Flop
        # Turn
        # River


if __name__ == "__main__":
    player1 = player("A")
    player2 = player("B")
    player3 = player("C")
    player4 = player("D")
    player5 = player("E")
    player6 = player("F")
    plist = [player1, player2, player3, player4, player5, player6]
    pass
    import sys
    print(sys.getdefaultencoding())
    # # Iterator test
    # itera = playerIterator(plist, 0)
    # for i in range(100):
    #     print(next(itera))

    # Deal Cards test
    table = Table()
    for i in plist:
        table.addPlayer(i)
    table.InitGame(debug=1)

    # Print board test
    # board = [Card.new('Ah'), Card.new("Kd")]
    # Card.print_pretty_card(Card.new('Ah'))
    # print(u'\u2660')
