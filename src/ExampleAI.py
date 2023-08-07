#!/usr/bin/env python3
# AI that plays checkers.

# IMPORTANT NOTE:
# For the game to recognize this as an
# AI, it's filename should have the words
# 'AI' in it.

__title__ = "Example Tic Tac Toe AI"
__author__ = "CoolCat467"
__version__ = "0.0.0"
__ver_major__ = 0
__ver_minor__ = 0
__ver_patch__ = 0

__game__ = "Tic Tac Toe"


REGISTERED = True
# Please send your finnished version of your AI to CoolCat467 at Github
# for review and testing and obain permission to change this flag to True


global BOARD


class Array(object):
    def __init__(self, rows=1, columns=1, initList=None):
        self.rows = int(rows)
        self.columns = int(columns)
        self._points = int(self.rows * self.columns)
        # self._data = [[]*self.rows]*self.columns
        self._data = {i: [None] * self.columns for i in range(self.rows)}
        if initList:
            if len(initList) != self._points:
                raise ValueError(
                    "Length of initialization list is not equal to %i."
                    % self._points
                )
            read = list(initList)
            for x in range(self.rows):
                self._data[x] = read[self.columns * x : self.columns * (x + 1)]

    def __repr__(self):
        data = [str(self._data[x]) for x in range(self.rows)]
        return "<Array [%s]>" % str(",\n" + " " * 8).join(data)

    def getRow(self, rowIndex):
        """Returns a copy of a row from the array."""
        x = int(rowIndex)
        if x > self.rows:
            raise IndexError("Row index out of range.")
        return self._data[x]

    def setRow(self, rowIndex, iterable):
        """Sets row at rowIndex to values from iterable."""
        x = int(rowIndex)
        if x > self.rows:
            raise IndexError("Row index out of range.")
        if len(iterable) != self.columns:
            raise ValueError(
                "Length of iterable is not equal to length of rows in array."
            )
        self._data[x] = list(iterable)

    def getColumn(self, columnIndex):
        """Returns a copy of a column from the array."""
        y = int(columnIndex)
        if y > self.columns:
            raise IndexError("Column index out of range.")
        return [self.getRow(x)[y] for x in range(self.rows)]

    def __getitem__(self, xy):
        """Get an item from array at row x column y."""
        if hasattr(xy, "__iter__"):
            x, y = xy
        else:
            raise ValueError("Index must be row index and column index!")
        if x > self.rows:
            raise IndexError("Row index out of range.")
        if y > self.columns:
            raise IndexError("Column index out of range.")
        return self.getRow(x)[y]

    def __setitem__(self, xy, value):
        """Set an item of array at row x column y to value."""
        if hasattr(xy, "__iter__"):
            x, y = xy
        else:
            raise ValueError("Index must be row index and column index!")
        if x > self.rows:
            raise IndexError("Row index out of range.")
        if y > self.columns:
            raise IndexError("Column index out of range.")
        self._data[x][y] = value

    def setColumn(self, columnIndex, iterable):
        """Sets column at columnIndex to values from iterable."""
        y = int(columnIndex)
        if y > self.columns:
            raise IndexError("Column index out of range.")
        if len(iterable) != self.rows:
            raise ValueError(
                "Length of iterable is not equal to length of columns in array."
            )
        for x, value in zip(range(self.rows), iter(iterable)):
            self[x, y] = value

    def __len__(self):
        return self._points

    def __iter__(self):
        return iter([self.getRow(x) for x in range(self.rows)])

    def __contains__(self, value):
        """Returns True if value in array."""
        return value in sum(iter(self), [])

    def index(self, value):
        """Return the first instance of value in self."""
        if value in self:
            for x in range(self.rows):
                if value in self.getRow(x):
                    y = self.getRow(x).index(value)
                    return x, y
        raise ValueError("%s is not in array" % value)


def safe(function):
    def safeFunction(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except BaseException as e:
            print("AI: Error: %s" % str(e))

    return safeFunction


PLANS = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


def getValidPlans(plans, board):
    yes = []
    for plan in plans:
        sucess = 0
        for pos in plan:
            data = board[pos]
            if data != 1:
                sucess += 1
        if sucess == 3:
            yes.append(plan)
    return yes


def getPossibleMutations(plan):
    data = []
    p = plan
    data.append([p[0], p[1], p[2]])
    data.append([p[0], p[2], p[1]])
    data.append([p[1], p[0], p[2]])
    data.append([p[1], p[2], p[0]])
    data.append([p[2], p[0], p[1]])
    data.append([p[2], p[1], p[0]])
    return data


def isValid(mutate, validPlans):
    yes = None
    mutations = getPossibleMutations(mutate)
    for plan in mutations:
        if plan in validPlans:
            yes = plan
            break
    return yes is None


def chooseGoodPlan(board):
    # Get the valid plans we can follow to win
    validPlans = getValidPlans(PLANS, board)
    # Pretty much convert all the plans into strings
    stringPlans = []
    for plan in validPlans:
        stringPlan = []
        for move in plan:
            string = " ".join(map(str, move))
            stringPlan.append(string)
        stringPlans.append(stringPlan)
    # We will find the moves with the highest number of plans dependant on them
    moves = {}
    # For each plan we can follow,
    for plan in stringPlans:
        # For each move of the plan
        for move in plan:
            # If the move is not in the move counts list
            if not move in moves:
                moves[move] = 1
            else:
                moves[move] += 1
    counts = list(reversed(sorted(moves.values())))
    moves2 = dict(moves)
    best = []
    for i in range(len(counts)):
        for key in iter(moves2):
            if moves2[key] == counts[0]:
                best.append(key)
                del moves2[key]
                del counts[0]
                break
    best = [tuple(map(int, i.split(" "))) for i in best]
    for able in [best[i:] + best[:i] for i in range(len(best))]:
        for part in [able[i : i + 3] for i in range(len(able))]:
            if isValid(part, BOARD["plays"]):
                print("part win")
                print(part)
                return part
    print("best win")
    print(best[:3])
    return best[:3]


@safe
def update(boardData):
    """This function is called by the game to inform the ai of any changes that have occored on the game board"""
    global BOARD, DATA
    board, plays = boardData
    DATA["last"] = BOARD["board"]
    BOARD = {"board": Array(3, 3, board), "plays": plays}
    print(BOARD["board"])


def turn():
    """This function is called when the game requests the AI to return the piece it wants to move's id and the tile id the target piece should be moved to."""
    global BOARD, DATA
    # If there are valid plays,
    if BOARD["plays"]:
        print("Taking Turn")
        # If we have a plan,
        if "plan" in DATA:
            print("We have plan")
            print(DATA["plan"])
            needNewPlan = bool(len(DATA["plan"]))
            # Can we still follow the plan?
            if False in [BOARD["board"][xy] == 0 for xy in DATA["plan"]]:
                print("We cannot follow plan")
                needNewPlan = True
        else:
            print("We have no plan")
            needNewPlan = True
        if needNewPlan:
            print("Choosing new plan")
            DATA["plan"] = chooseGoodPlan(BOARD["board"])
            print("New plan:")
            print(DATA["plan"])
        for i in range(len(DATA["plan"])):
            play = DATA["plan"][i]
            print(play)
            if play in BOARD["plays"]:
                print("Previous is win.")
                del DATA["plan"][i]
                return play
    # Otherwise, send that we don't know what to do.
    return None
    # In extreme cases, it may be necessary to quit the game,
    # for example, if your AI connects to the internet in some way.
    # In this case, you can also return 'QUIT', but PLEASE,
    # ONLY USE THIS IF IT IS TRULY NECESSARY


@safe
def turnSuccess(tf):
    """This function is called immidiately after the ai's play is made, telling it if it was successfull or not"""
    if not tf:
        print("AI: Something went wrong playing move...")


@safe
def stop():
    """This function is called immidiately after the game's window is closed"""
    pass


@safe
def init():
    """This function is called immidiately after the game imports the AI. Not required to exist."""
    # We dunno what the board looks like, so set it to blank.
    global BOARD, DATA
    BOARD = {"board": None}
    DATA = {}


print("AI: AI Module Loaded")
print("AI: " + __title__ + " Created by " + __author__)
