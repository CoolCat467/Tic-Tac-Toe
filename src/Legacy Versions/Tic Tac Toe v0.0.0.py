#!/usr/bin/env python
# Program that plays tic tac toe.

# isPrime Thanks to Anivargi's Twin prime calculator at
# scratch.mit.edu/projects/128640110/ for the program that
# finds out if it is prime or not.

NAME = "Tic Tac Toe"
__version__ = "0.0.0"

import os
import sys
import time
from pathlib import Path
from random import randint as rand

global justplayed
global startTime
global PRIMENUMBER
global SYSNAME
global NODENAME
global CURFOLD
global AICAN
global catone
global liii
global lii
global li

startTime = 0
PRIMENUMBER = 2227507  # For Hashing

liii = [0, 0, 0]
lii = [0, 0, 0]
li = [0, 0, 0]

# 31 32 33
# 21 22 23
# 11 12 13


class doMath:
    def isPrime(num):
        # Anivargi's program that finds out if it is prime or not. See top
        isPrime = True
        if num < 3 or num == 3:
            isPrime = True
        else:
            divideNumber = 2
            while isPrime == True and divideNumber != math.ceil(
                math.sqrt(num + 1)
            ):
                if num % divideNumber == 0:
                    isPrime = False
                else:
                    divideNumber = divideNumber + 1
        return isPrime

    def timeCalc(totalsec):
        # Calculate Time
        # Min Calc
        if totalsec >= 60:
            totalmin = totalsec / 60
            if totalmin < 1:
                totalmin = 0
            else:
                totalmin = int(round(totalmin))
        else:
            totalmin = 0
            totalhr = 0
        # Hr Calc
        if totalmin >= 60:
            totalhr = totalmin / 60
            if totalhr < 0:
                totalhr = 0
            else:
                totalhr = int(round(totalhr))
        else:
            totalhr = 0
        # Update min value
        for i in range(totalhr):
            totalmin = totalmin - 60
        # Update sec value
        i = None
        for i in range(totalmin):
            totalsec = totalsec - 60
        return "Total Time Running: %s hrs, %s mins, %s secs" % (
            totalhr,
            totalmin,
            abs(totalsec),
        )

    def getnums(text):
        # make a string into a number string
        nums = ""
        for letter in text.upper():
            num = ord(letter) - 32
            if num < 10:
                num = "0" + str(num)
            nums = str(nums) + str(num)
        return int(nums)

    def getext(nums):
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

    def gethashed(text):
        # Take the entered text, hash it, and return it
        intstr = doMath.getnums(text)
        choose = 2
        data = ""
        intstr = int(intstr) * PRIMENUMBER
        for num in str(intstr):
            if choose % 2 != "0":
                data = str(data) + str(num)
            choose = choose + 1
        intstr = int(data) * PRIMENUMBER

        while len(str(intstr)) < 20:
            intstr = intstr * PRIMENUMBER
        if len(str(intstr)) > 20:
            choose = 0
            data = ""
            for i in str(intstr):
                choose = choose + 1
                if choose < 20:
                    data = str(data) + str(i)
                else:
                    data = int(data) * (int(i) + 1)
                    # data = data
            intstr = int(data)
        return doMath.getext(intstr)

    def partquotes(text, witch, how=False):
        """takes input, like "I think 'cats' are so 'cool' yay",
        in input text, which defines which part im quotes
        of 'cats' and 'cool' gets returned. if how is set True,
        it takes text input, which is ignored, and it returns
        howmany parts are in quotes in the text."""
        ftimes = 0
        found = False
        for i in text:
            if not found:
                if i == "'":
                    found = True
                    ftimes = ftimes + 1
                    var = "l" + str("i" * ftimes)
                    exec("%s = ''" % var)
                    to = "%s = %s + " % (var, var)
            else:
                if i != "'":
                    exec(str(to) + "'" + i + "'")
                else:
                    found = False
        var = "l" + str("i" * int(witch))
        if not how:
            toreturn = eval(var)
        else:
            toreturn = ftimes
        return toreturn

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
        wlist = str("l" + ("i" * int(locx)))
        act = str(wlist + "[i]")
        for i in range(int(len(eval(wlist)))):
            part = str("pt" + ("i" * (i + 1)) + " = ")
            exec(str(part + str(eval(act))))
        part = str("pt" + ("i" * int(locy)))
        if int(eval(part)) == 0 or int(pid) == 0:
            exec(str(part + " = " + str(pid)))
            for i in range(3):
                exec(str("del " + wlist + "[0]"))
            firstpt = str(wlist + ".append(")
            exec("global " + wlist)
            for i in range(3):
                part = str("pt" + ("i" * (i + 1)))
                exec(str(firstpt + part + ")"))
            toret = True
        else:
            toret = False
        return toret

    def printdata():
        # program that prints the game board
        # 31 32 33
        # 21 22 23
        # 11 12 13
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
                if line == "0":
                    linep = linep + "_"
                elif line == "1":
                    linep = linep + "X"
                elif line == "2":
                    linep = linep + "O"
                else:
                    linep = linep + "_"
                    play(0, tmpx, tmpy)

                if ii < 2:
                    linep = linep + " "
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
        toret = False
        if turn == 1:
            player = "X"
        if turn == 2:
            player = "O"
        print("%s's Turn" % player)
        print("")
        game.printdata()
        print("")
        posx = input(
            "What row would you like to play %s in? (A, B, C) " % player
        )
        posy = input(
            "What collom would you like to play %s in? (1, 2, 3) " % player
        )
        print("")
        if posx != "A" and posx != "B" and posx != "C":
            print("Try Again")
            print("")
            toret = True
        else:
            if posy != "1" and posy != "2" and posy != "3":
                print("Try Again")
                print("")
                toret = True
            else:
                posx = int(4 - int(ord(posx) - 64))
                try:
                    justplayed = str(str(posx) + str(posy) + str(turn))
                    success = game.play(turn, posx, posy)
                except NameError:
                    print("Try Again")
                    print("")
                    toret = True
                else:
                    posx = chr(int(4 - posx) + 64)
                    if success:
                        print(
                            "Played %s in row %s, collom %s."
                            % (player, posx, posy)
                        )
                        print("")
                    else:
                        print(
                            "That spot is not playable. Please enter another location."
                        )
                        print("")
                        toret = True
        return toret

    def check():
        # program that checks for wins and cats (sadly not real cats) :(
        # only game cats
        global catone
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
            catone = True
        else:
            catone = False
        return izit

    def start(mode):
        # program that starts everything
        global justplayed
        if mode == "REG":
            pturn = rand(1, 2)
            won = False
            while not won:
                if pturn == 1:
                    pturn = 2
                elif pturn == 2:
                    pturn = 1
                if game.turn(pturn):
                    cat = game.turn(pturn)
                won = game.check()
                if not won:
                    won = catone
        elif mode == "AI":
            import TicAI

            print("")
            TicAI.start()
            print("")
            pturn = rand(1, 2)
            justplayed = 220
            won = False
            times = 0
            while not won:
                if pturn == 1:
                    pturn = 2
                elif pturn == 2:
                    pturn = 1
                # compile and send data
                send = doMath.getnums(str(justplayed))
                diditwork = TicAI.update(send)
                if not diditwork:
                    while not diditwork:
                        diditwork = TicAI.update(send)
                        print("TicTacToe: ERR: AI Update Unsuccessful")
                        time.sleep(1)
                if pturn == 1:
                    # player turn
                    notgoodplay = True
                    while notgoodplay:
                        notgoodplay = game.turn(pturn)
                else:
                    # recieve and decode data
                    recdata = TicAI.turn()
                    decdata = doMath.getext(recdata)
                    # play AI's turn
                    locx = str(decdata[0])
                    locy = int(decdata[1])
                    posx = int(4 - (ord(locx) - 64))
                    success = game.play(2, posx, locy)
                    if not success:
                        tempjustplayed = justplayed
                        while not success:
                            TicAI.update(doMath.getnums(str(tempjustplayed)))
                            recdata = TicAI.turn()
                            decdata = doMath.getext(recdata)
                            locx = str(decdata[0])
                            locy = int(decdata[1])
                            posx = int(4 - (ord(locx) - 64))
                            success = game.play(2, posx, locy)
                            time.sleep(1)
                    justplayed = str(str(posx) + str(locy) + str(2))
                    print("AI Played O in row %s, collom %s." % (locx, locy))
                    print("")
                won = game.check()
                if not won:
                    won = catone
                times = int(times + 1)
        print("")
        if catone:
            print("Cat won this round!")
            print("Tie!")
        else:
            print("Player %s won this round!" % pturn)
        print("")
        game.printdata()
        print("")
        print("Reseting...")
        for i in range(3):
            for ii in range(3):
                game.play(0, int(i + 1), int(ii + 1))
        print("Done!")

    def main():
        # main script
        global AICAN
        # Start Main Script
        if AICAN:
            print("TicAI.py found in the folder")
            print("this program is being run from!")
            print("Play against AI? (y/n)")
            playai = str(input(""))
            print("")
            if playai != "y" and playai != "n":
                print("Try Again")
                print("")
                game.main()
            elif playai == "n":
                print("Ok!")
                AICAN = False
                game.main()
            else:
                print("Ok!")
                print("")
                print("Player 1 = X")
                print("AI = O")
                print("Starting Game!")
                print("")
                game.start("AI")
        else:
            print("")
            print("Player 1 = X")
            print("Player 2 = O")
            print("Starting Game!")
            print("")
            game.start("REG")
        # Ask if you want to quit
        cont = str(input("Do you want to quit? (y/n) "))
        print("")
        if cont == "y":
            runningMain = False
        else:
            runningMain = True
        if runningMain:
            print("Excellent!")
            print("")
            print("")
        else:
            print(doMath.timeCalc(int(round(time.time() - startTime))))
            sys.exit()

    pass


def loop():
    # loop game.main()
    if runningMain:
        game.main()
        loop()


def filexists(filename, cwd):
    # check for if files exist
    try:
        (Path(str(cwd) + "/" + str(filename))).resolve()
    except FileNotFoundError:
        return False
    else:
        return True


def main():
    # true main
    # Greet user
    print("Welcome to the Tic Tac Toe Program v1.5!")
    print("Copywrite Cat Ink, all rights reserved.")
    print()
    print("Beginning startup...")
    # Setup some globals
    global SYSNAME
    global NODENAME
    global CURFOLD
    global runningMain
    global AICAN
    SYSNAME = doMath.partquotes(str(os.uname()), 1)
    NODENAME = doMath.partquotes(str(os.uname()), 2)
    CURFOLD = doMath.partquotes(str(os.path.split(str(os.getcwd()))), 2)
    folder = doMath.partquotes(str(os.path.split(os.getcwd())), 2)
    runningMain = True
    AICAN = False
    if filexists("TicAI.py", os.getcwd()):
        AICAN = True
    # Start the loop
    loop()


# Activation Program
if __name__ == "__main__":
    startTime = time.time()
    print("Copywrite Cat Inc, All rights reserved.")
    print("Programmed by CoolCat467")
    try:
        main()
    except KeyboardInterrupt:
        print("Quitter!")
else:
    startTime = time.time()
    print("Game Module Loaded")
    # for fuzzball implementation
