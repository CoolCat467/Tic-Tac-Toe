#!/usr/bin/env python
# Program that plays tic tac toe.

import os
from random import randint as rand
from shutil import copyfile

NAME = "Tic Tac Toe"
__version__ = "0.0.1"

global justplayed
global startTime
global PRIMENUMBER
global SYSNAME
global NODENAME
global CURFOLD
global AICAN
global catwon
global liii
global lii
global li

liii = [0, 0, 0]
lii = [0, 0, 0]
li = [0, 0, 0]

# 31 32 33
# 21 22 23
# 11 12 13


class conv:
    def toNums(text):
        # make a string into a number string
        nums = ""
        for letter in str(text).upper():
            num = ord(letter) - 32
            if num < 10:
                num = "0" + str(num)
            nums = str(nums) + str(num)
        return int(nums)

    def toText(nums):
        # make a number string into text
        control = 1
        prev = ""
        text = ""
        for number in str(nums):
            if bool(control):
                prev = str(number)
                control = 0
            else:
                if prev == 0:
                    num = number
                else:
                    num = prev + str(number)
                text = str(text)
                if num == "0":
                    text = text + " "
                else:
                    text = text + chr(int(num) + 32)
                control = 1
        return text

    pass


class game:
    def getCordInf(x, y):
        # return data about the given playing choordinits
        wlist = str("l" + ("i" * y))
        act = str(wlist + "[" + str(int(x) - 1) + "]")
        return int(eval(act))

    def play(pid, locx, locy):
        # play an X, O, or blank at a location.
        # pid = play ID, 2, 1, or 0, corspoding to O, X, and blank
        global liii
        global lii
        global li
        # program that plays moves
        toret = False
        wlist = str("l" + ("i" * int(locx)))  # which list = li, lii, or liii
        act = str(wlist + "[i]")
        for i in range(
            len(eval(wlist))
        ):  # for each peice of data in the selected list
            part = str(
                "pt" + ("i" * (i + 1)) + " = "
            )  # select part 1-3 for exec
            exec(
                str(part + str(eval(act)))
            )  # part 1-3 = position at that point
        part = str("pt" + ("i" * int(locy)))  # selected part = part 1-3
        if (
            int(eval(part)) == 0 or int(pid) == 0
        ):  # if selected part is 0 or write data is 0
            exec(
                str(part + " = " + str(pid))
            )  # part at that position is write data
            for i in range(3):
                exec(str("del " + wlist + "[0]"))  # delete all data
            exec("global " + wlist)  # global the list for exec
            firstpt = str(wlist + ".append(")  # selected list .append(
            for i in range(3):
                part = str("pt" + ("i" * (i + 1)))  # part = pt 1-3
                exec(
                    str(firstpt + part + ")")
                )  # execute append part to selected list
            toret = True  # we updated positions correctly
        return toret

    def printdata():
        # program that prints the game board
        # 31 32 33
        # 21 22 23
        # 11 12 13
        convrt = {"0": "_", "1": "X", "2": "O"}
        print("    1 2 3")
        print("  =========")
        for i in range(3):
            tmpy = 3 - i  # As 123 would print backwords, this
            # makes it go from 123 => 321
            linep = " = "
            for ii in range(3):
                tmpx = 1 + ii  # 123
                line = "" + str(game.getCordInf(tmpx, tmpy))  # 123, 321
                # print('%s %s %s' % (tmpx, tmpy, line))
                if line in tuple(convrt.keys()):
                    linep += convrt[line]
                else:
                    linep += "_"
                    play(0, tmpx, tmpy)

                if ii < 2:
                    linep += " "
                else:
                    letter = chr(i + 65)
                    linep = letter + linep + " ="

            print(linep)
        print("  =========")

    def turn(turn):
        # program that runs fot each person's turn
        global liii
        global lii
        global li
        global success
        global justplayed
        while True:
            loop = False
            if turn == 1:
                player = "X"
            if turn == 2:
                player = "O"
            print("%s's Turn.\n" % player)
            game.printdata()
            posx = input(
                "\nWhat row would you like to play %s in? (A, B, C) " % player
            )
            posy = input(
                "What collom would you like to play %s in? (1, 2, 3) " % player
            )
            print("")
            if not (
                (posx.upper() in ("A", "B", "C")) and (posy in ("1", "2", "3"))
            ):
                loop = True
            else:
                posx = int(4 - int(ord(posx.upper()) - 64))
                try:
                    justplayed = str(str(posx) + str(posy) + str(turn))
                    success = game.play(turn, posx, posy)
                except NameError:
                    loop = True
                else:
                    posx = chr(int(4 - posx) + 64)
                    if success:
                        print(
                            "Played %s in row %s, collom %s.\n"
                            % (player, posx, posy)
                        )
                    else:
                        print("That spot is not playable.")
                        loop = True
            if loop:
                print("Please Try Again.\n")
            else:
                break

    def check():
        # program that checks for wins and cats (sadly not real cats) :(
        # only game cats
        global catwon
        # Y
        # 31 32 33
        # 21 22 23
        # 11 12 13 X
        izit = False
        # side to side check
        for i in range(1, 4):
            lineData = ""
            getyval = 4 - i
            for ii in range(1, 4):
                getxval = ii
                lineData = lineData + str(game.getCordInf(getxval, getyval))
            if str(lineData) == "222":
                izit = True
            elif str(lineData) == "111":
                izit = True
        # up down check
        for i in range(1, 4):
            lineData = ""
            getxval = 4 - i
            for ii in range(1, 4):
                getyval = ii
                lineData = lineData + str(game.getCordInf(getxval, getyval))
            if str(lineData) == "222":
                izit = True
            elif str(lineData) == "111":
                izit = True
        # diaginal check
        linelist = []
        tmp = str(str(liii[0]) + str(lii[1]) + str(li[2]))
        linelist.append(tmp)
        tmp = str(str(li[0]) + str(lii[1]) + str(liii[2]))
        linelist.append(tmp)
        for i in range(2):
            lineData = int(linelist[i])
            if str(lineData) == "222":
                izit = True
            elif str(lineData) == "111":
                izit = True
        # check for cat
        plans = ["CA", "CB", "CC", "RA", "RB", "RC", "DA", "DB"]  # All Plans
        CA = ["A1", "A2", "A3"]
        CB = ["B1", "B2", "B3"]
        CC = ["C1", "C2", "C3"]
        RA = ["A1", "B1", "C1"]
        RB = ["A2", "B2", "C2"]
        RC = ["A3", "B3", "C3"]
        DA = ["A1", "B2", "C3"]
        DB = ["A3", "B2", "C1"]
        count = 0
        for i in range(2):
            whofor = int(i) + 1
            badones = []
            for ii in plans:
                dalist = eval(ii)
                times = 0
                for iii in dalist:
                    data = int(
                        game.getCordInf(int(ord(iii[0]) - 64), int(iii[1]))
                    )
                    if data == whofor or data == 0:
                        times = times + 1
                if times != 3:
                    badones.append(ii)
            if len(badones) == len(plans):
                count = count + 1
        if count == 2:
            izit = True
            catwon = True
        else:
            catwon = False
        return izit

    def playRegular(pturn):
        global catwon
        won = False
        while not (won or catwon):
            if pturn == 1:
                pturn = 2
            elif pturn == 2:
                pturn = 1
            game.turn(pturn)
            won = game.check()
        return pturn

    def playAI(pturn):
        global catwon
        global justplayed
        pturn = rand(1, 2)
        justplayed = 220
        won = False
        times = 0
        while not (won or catwon):
            if pturn == 1:
                pturn = 2
            elif pturn == 2:
                pturn = 1
            if pturn == 1:
                # player turn
                notgoodplay = True
                game.turn(pturn)
            else:
                # recieve and decode data
                recdata = TicAI.turn()
                # play AI's turn
                locx, locy = conv.toText(recdata)
                posx = int(4 - (ord(locx) - 64))
                success = game.play(2, posx, locy)
                if not success:
                    tempjustplayed = conv.toNums(str(justplayed))
                    while not success:
                        TicAI.update(tempjustplayed)
                        recdata = TicAI.turn()
                        locx, locy = conv.toText(recdata)
                        posx = int(4 - (ord(locx) - 64))
                        success = game.play(2, posx, locy)
                justplayed = str(str(posx) + str(locy) + str(2))
                print("AI Played O in row %s, collom %s.\n" % (locx, locy))
            # send data to ai
            TicAI.update(conv.toNums(justplayed))
            # check for win
            won = game.check()
            times += 1
        return pturn

    def start(mode):
        # program that starts everything
        global catwon
        catwon = False
        pturn = rand(1, 2)
        if mode == "REG":
            pturn = game.playRegular(pturn)
        elif mode == "AI":
            pturn = game.playAI(pturn)
        if catwon:
            print("\nCat won this round!\nTie!")
        else:
            print("\nPlayer %s won this round!" % pturn)
        print("\nFinal Board:")
        game.printdata()
        print("\nReseting...")
        for i in range(3):
            for ii in range(3):
                game.play(0, int(i + 1), int(ii + 1))
        print("Done!")

    def main():
        # main script
        global AICAN
        # Start Main Script
        if AICAN:
            print("AIs were found in the folder")
            print("this program is being run from!")
            print("\nPlay against an AI? (y/n)")
            playai = str(input(""))
            print("")
            if not playai.lower() in ("y", "n"):
                print("Try Again\n")
                game.main()
            elif playai == "n":
                print("Ok!")
                game.start("REG")
            else:
                ais = findAis()
                if len(ais) > 1:
                    print("Which AI do you want to play against?")
                    for i in range(len(ais)):
                        print(str(i + 1) + ". " + ais[i])
                    while True:
                        number = input("AI Number: ")
                        try:
                            number = int(number)
                        except ValueError:
                            continue
                        if type(number) == type(1):
                            if int(number - 1) in range(len(ais)):
                                break
                else:
                    number = 0
                ai = findAis()[number - 1]
                print("\nSelected AI '" + ai + "'\nLoading AI...\n")
                loadAI(ai)
                print("\nPlayer 1 = X\nAI = O\nStarting Game!\n")
                game.start("AI")
        else:
            print("\nPlayer 1 = X")
            print("Player 2 = O")
            print("Starting Game!\n")
            game.start("REG")
        # Ask if you want to quit
        cont = str(input("\nDo you want to quit? (y/n) "))
        print("")
        runningMain = False
        if cont != "y":
            print("Excellent!\n\n")
            runningMain = True

    pass


def loop():
    # loop game.main()
    if runningMain:
        game.main()
        loop()


def loadAI(name):
    if name in findAis():
        copyfile(name + ".py", "temp.py")
        global TicAI
        import temp as TicAI

        TicAI.init()


def findAis():
    ais = []
    for filename in os.listdir(os.getcwd()):
        if ".py" in filename and "AI" in filename:
            ais.append("".join(filename.split(".py")))
    return ais


def main():
    # true main
    # Greet user
    print("Welcome to the " + NAME + " Program v" + __version__ + "!")
    print("Copywrite Cat Ink, all rights reserved.")
    print("\nBeginning startup...")
    # Setup some globals
    global SYSNAME
    global NODENAME
    global CURFOLD
    global runningMain
    global AICAN
    # SYSNAME =
    # NODENAME =
    # CURFOLD =
    # folder =
    runningMain = True
    AICAN = bool(len(findAis()) >= 1)
    # Start the loop
    loop()
    os.sys.exit()


# Activation Program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
else:
    print("Game Module Loaded")
    # for fuzzball implementation
