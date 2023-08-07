#!/usr/bin/env python
# Program that plays tic tac toe, graphically.

import math
import os
import sys
import time
from pathlib import Path
from random import randint as rand
from tkinter import *

PREBOOTERR = ""
try:
    import maths
except ImportError:
    PREBOOTERR = "Maths Module Failed to Import"

global SIZE
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

SIZE = 400
startTime = 0
PRIMENUMBER = 2227507  # For Hashing

liii = [0, 0, 0]
lii = [0, 0, 0]
li = [0, 0, 0]

# 31 32 33
# 21 22 23
# 11 12 13

tk = Tk()
tk.title("Tic Tac Toe")
tk.resizable(0, 0)
# tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=SIZE, height=SIZE, bd=0, highlightthickness=0)
canvas.pack()
canvas.update()


class game:
    def gprint(toprint, x, y, size=15, color="black"):
        canvas.create_text(
            x, y, text=toprint, font=("Times", size), fill=color
        )
        canvas.pack()
        canvas.update()

    def circle(x, y, r, w):
        canvas.create_oval(x + r, y + r, x - r, y - r, width=width)
        canvas.pack()
        canvas.update()

    def cross(x, y, r, w):
        # w = width, l = length
        canvas.create_line(x - l, y - l, x + l, y + l, width=w)
        canvas.pack()
        canvas.update()
        canvas.create_line(x + l, y - l, x - l, y + l, width=w)
        canvas.pack()
        canvas.update()

    def box(x, y, r, w):
        # r = raius, w = width
        xi = int(x - r)
        yi = int(y - r)
        xii = int(x + r)
        yii = int(y + r)
        canvas.create_polygon(
            xi,
            yii,
            xii,
            yii,
            xii,
            yi,
            xi,
            yi,
            fill="",
            outline="black",
            width=w,
        )

    def drawBoard():
        size = int(round(SIZE / 4))
        w = float(SIZE * 0.01)
        add = int(round(size / 2))
        for i in range(2):
            for ii in range(2):
                x = (int(ii) * size) + (add + size)
                y = (int(i) * size) + (size)
                # print(str(tuple([x, y])))
                game.box(x, y, size, w)

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
                send = maths.getnums(str(justplayed))
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
                    decdata = maths.getext(recdata)
                    # play AI's turn
                    locx = str(decdata[0])
                    locy = int(decdata[1])
                    posx = int(4 - (ord(locx) - 64))
                    success = game.play(2, posx, locy)
                    if not success:
                        tempjustplayed = justplayed
                        while not success:
                            TicAI.update(maths.getnums(str(tempjustplayed)))
                            recdata = TicAI.turn()
                            decdata = maths.getext(recdata)
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
            print(maths.timeCalc(int(round(time.time() - startTime))))
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
    SYSNAME = maths.partquotes(str(os.uname()), 1)
    NODENAME = maths.partquotes(str(os.uname()), 2)
    CURFOLD = maths.partquotes(str(os.path.split(str(os.getcwd()))), 2)
    folder = maths.partquotes(str(os.path.split(os.getcwd())), 2)
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
    print("Programmed by CoolCat467.")
    try:
        main()
    except KeyboardInterrupt:
        print("Quitter!")
else:
    startTime = time.time()
    print("Game Module Loaded")
    # for fuzzball implementation
