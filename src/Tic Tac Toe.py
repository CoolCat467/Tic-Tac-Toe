#!/usr/bin/env python3
# Tic Tac Toe game
# -*- coding: utf-8 -*-

# Programmed by CoolCat467

import importlib
import os
from random import randint

##try:
##    from array2 import *
##except ImportError:
##    print('Array module not found. Please ensure you did not remove/rename/move any files from the game folder.')
##    os.abort()

__title__ = "Tic Tac Toe"
__author__ = "CoolCat467"
__version__ = "1.0.0"
__ver_major__ = 1
__ver_minor__ = 0
__ver_patch__ = 0


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

    def get_row(self, rowIndex):
        """Returns a copy of a row from the array."""
        x = int(rowIndex)
        if x > self.rows:
            raise IndexError("Row index out of range.")
        return self._data[x]

    def get_column(self, columnIndex):
        """Returns a copy of a column from the array."""
        y = int(columnIndex)
        if y > self.columns:
            raise IndexError("Column index out of range.")
        return [self.get_row(x)[y] for x in range(self.rows)]

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
        return self.get_row(x)[y]

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

    pass


class Game(object):
    """Game board"""

    def __init__(self):
        self.board = Array(3, 3, [0] * 9)
        self.cturn = 0
        self.won = None
        self.ai = None
        self.active = False

    def get_coord_info(self, x, y):
        """Return data about given choordinates."""
        return self.board[x, y]

    def play(self, x, y, pid):
        """Play a piece at x, y."""
        at = self.board[x, y]
        if at == 0 or pid == 0:
            self.board[x, y] = int(pid)
            return True
        return False

    def print_board(self, prnt=True):
        """Print the game board."""
        convert = "_XO"
        string = "    1 2 3\n  =========\n"
        for y in range(3):
            cline = chr(y + 65) + " = "
            for x in range(3):
                cline += convert[self.board[x, y]] + " "
            string += cline + "=\n"
        string += "  ========="
        if prnt:
            print(string)
        else:
            return string

    def turn(self):
        """Take a turn"""
        loop = True
        while loop:
            if self.cturn == 1:
                player = "X"
            if self.cturn == 2:
                player = "O"
            print("%s's Turn.\n" % player)
            self.print_board()
            posy = input(
                "\nWhat row would you like to play %s in? (A, B, C) " % player
            )
            posx = input(
                "What column would you like to play %s in? (1, 2, 3) " % player
            )
            print("")
            if (posy.upper() in ("A", "B", "C")) and (posx in ("1", "2", "3")):
                x = int(posx) - 1
                y = ord(posy.upper()) - 65
                success = self.play(x, y, self.cturn)
                if success:
                    print(f"Played {player} in row {posy}, column {posx}.\n")
                    loop = False
                else:
                    print("That spot is not playable.")
            if loop:
                print("Please Try Again.\n")

    def check(self):
        """Check for wins and cat wins"""

        # row check
        for y in range(3):
            row = "".join(map(str, self.board.get_row(y)))
            if row == "222":
                self.won = 2
                return True
            elif row == "111":
                self.won = 1
                return True
        # column check
        for x in range(3):
            column = "".join(map(str, self.board.get_column(x)))
            if column == "222":
                self.won = 2
                return True
            elif column == "111":
                self.won = 1
                return True
        # diaginal check
        positions = (((0, 0), (1, 1), (2, 2)), ((2, 0), (1, 1), (0, 2)))
        for poslst in positions:
            get = lambda xy: self.get_coord_info(xy[0], xy[1])
            data = "".join(map(str, map(get, poslst)))
            if data == "222":
                self.won = 2
                return True
            elif data == "111":
                self.won = 1
                return True
        # check for cat
        plans = (
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0)),
        )
        count = 0
        for player in range(1, 3):
            badones = []
            for plan in plans:
                times = 0
                for position in plan:
                    data = self.board[position]
                    if data == player or data == 0:
                        times += 1
                if times != 3:
                    badones.append(plan)
            if len(badones) == len(plans):
                count += 1
        if count == 2:
            self.won = 3
            return True
        return False

    def play_regular(self):
        """Play a regular game of two player tic tac toe."""
        while not (self.won):
            self.cturn = (self.cturn) % 2 + 1
            self.turn()
            self.check()

    def get_valid_plays(self):
        """Return a list of valid plays."""
        plays = [(x, y) for x in range(3) for y in range(3)]
        valid = []
        for play in plays:
            if self.board[play] == 0:
                valid.append(play)
        return valid

    def get_board_data(self):
        """Return a copy of board data. Sent to AI."""
        data = []
        ##        for y in range(3):
        ##            for x in range(3):
        for x in range(3):
            for y in range(3):
                data.append(self.board[x, y])
        return list(data), self.get_valid_plays()

    def _falureMeansPlayerWin(function):
        def safeFunction(self, *args, **kwargs):
            try:
                function(self, *args, **kwargs)
            except KeyboardInterrupt:
                raise
            except BaseException as e:
                print("An Error occored: %s. Player wins!" % str(e))
                self.won = 1

        return safeFunction

    ##    @_falureMeansPlayerWin
    def play_ai(self):
        """Play a game of Tic Tac Toe against an AI."""
        passes = 0
        while not (self.won):
            self.cturn = (self.cturn) % 2 + 1
            self.ai.update(self.get_board_data())
            if self.cturn == 1:
                self.turn()
            else:
                read = self.ai.turn()
                if read is None:
                    self.cturn -= 1
                    passes += 1
                    if passes > 5:
                        print(
                            "AI passed more than five times. Player automatically wins!"
                        )
                        self.won = 1
                        break
                    else:
                        print("AI passed turn.")
                elif read == "QUIT":
                    print("AI has quit the game. Player automatically wins!")
                    self.won = 1
                    break
                else:
                    if hasattr(read, "__iter__"):
                        data = list(read)
                        if len(data) != 2:
                            print(
                                "AI returned invalid data as play data. Player automatically wins!"
                            )
                            self.won = 1
                            break
                        x, y = data
                        success = self.play(x, y, self.cturn)
                        if hasattr(self.ai, "turnSuccess"):
                            self.ai.turnSuccess(success)
                        if not success:
                            self.cturn -= 1
                        else:
                            print("AI took its turn")
                    else:
                        print(
                            "AI returned non-iterable object as play data. Player automatically wins!"
                        )
                        self.won = 1
                        break
            self.check()
        if hasattr(self.ai, "stop"):
            self.ai.stop()
        del self.ai
        self.ai = None

    def start_game(self):
        """Start the game"""
        self.cturn = randint(1, 2)
        self.won = 0
        AI = False
        if self.ai is None:
            self.play_regular()
        else:
            AI = True
            self.play_ai()
        if self.won == 3:
            print("\nCat won this round!\nTie!")
        elif AI:
            if self.won == 1:
                print("\nPlayer won this round!")
            else:
                print("\nAI won this round!")
        else:
            print("\nPlayer %s won this round!" % str(self.won))
        print("\nFinal Board:")
        self.print_board()
        print("\nReseting...")
        for y in range(3):
            for x in range(3):
                self.play(x, y, 0)
        print("Done!")

    def run(self):
        """Main loop while self.active"""
        self.active = True
        while self.active:
            # main script
            # Start Main Script
            twoplayer = True
            scanpath = os.path.split(__file__)[0]
            ais = [
                i.split(".")[0]
                for i in os.listdir(scanpath)
                if "." in i and i.split(".")[1] == "py" and "AI" in i
            ]
            if ais:
                print(
                    "AI files found in this folder!\nWould you like to play against an AI?"
                )
                do = input("(y/n) : ").lower()
                if do == "y":
                    print("\nList of AIs found:")
                    for num, name in zip(range(len(ais)), ais):
                        print("%i : %s" % (num + 1, name))
                    print("\nWhich AI would you like to play against?")
                    num = input("(1 to %i) : " % len(ais))
                    print()
                    if num.isdigit():
                        num = int(num) - 1
                        if num < len(ais):
                            name = ais[num]
                            self.ai = importlib.import_module(name)
                            print()
                            go = False
                            if not hasattr(self.ai, "__game__"):
                                print(
                                    "AI does not have the game it plays specified!"
                                )
                            elif not hasattr(self.ai, "update") or not hasattr(
                                self.ai, "turn"
                            ):
                                print(
                                    "AI does not have update and/or turn functions!"
                                )
                            else:
                                if not self.ai.__game__ == __title__:
                                    print(
                                        'AI plays "%s", not %s!'
                                        % (self.ai.__game__, __title__)
                                    )
                                else:
                                    go = True
                                    if hasattr(self.ai, "init"):
                                        self.ai.init()
                                    name = "Loaded AI"
                                    if hasattr(self.ai, "__title__"):
                                        name = str(self.ai.__title__)
                                    print("Player 1  = X")
                                    print("%s = O" % name)
                                    print("\nStarting Single Player Game!\n")
                                    twoplayer = False
                            if not go:
                                author = " "
                                if hasattr(self.ai, "__author__"):
                                    author = (
                                        ", " + str(self.ai.__author__) + ", "
                                    )
                                print(
                                    "Contact the developer of the AI%sand tell them about this issue."
                                    % author
                                )
                        else:
                            print("That is an invalid number.")
                    else:
                        print("That is an invalid number.")
            if twoplayer:
                print("\nPlayer 1 = X")
                print("Player 2 = O")
                print("Starting Two Player Game!\n")
                if not self.ai is None:
                    self.won = 1
                    self.play_ai()
            self.start_game()
            # Ask if you want to quit
            cont = str(input("\nDo you want to quit? (y/n) : "))
            if cont.lower() != "y":
                print("\nExcellent!\n\n")
            else:
                self.active = False

    pass


def run():
    global game
    game = Game()
    game.run()
    print("\nHave a nice day!")


# Activation Program
if __name__ == "__main__":
    print(f"{__title__} v{__version__}\nProgrammed by {__author__}.\n")
    try:
        run()
    except KeyboardInterrupt:
        print("Exiting...")
