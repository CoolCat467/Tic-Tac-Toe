#!/usr/bin/env python
# AI that plays tic tac toe.

# Programmed by CoolCat467

NAME = "AI"
author = "CoolCat467"
registered = True
__version__ = "0.0.1"

__game__ = "Tic Tac Toe"

import math
import os
import random

global lists
global cliii
global clii
global cli
global plan
global pplans
global ppplans
global lpplan
global plans
global CA
global CB
global CC
global RA
global RB
global RC
global DA
global DB
global ptofplay  # part of plan to play
global custmove  # custom move data (set with plan = 'CM')
cliii = [0, 0, 0]  # ai's equivelent to liii
clii = [0, 0, 0]  # ai's equivelent to lii
cli = [0, 0, 0]  # ai's equivelent to li
pplans = []  # ai possible plans
plan = ""  # ai current plan
ppplans = []  # player's possible plans
lpplan = ""  # player's likely plan
plans = ["CA", "CB", "CC", "RA", "RB", "RC", "DA", "DB"]  # All Plans
CA = ["A1", "A2", "A3"]
CB = ["B1", "B2", "B3"]
CC = ["C1", "C2", "C3"]
RA = ["A1", "B1", "C1"]
RB = ["A2", "B2", "C2"]
RC = ["A3", "B3", "C3"]
DA = ["A1", "B2", "C3"]
DB = ["A3", "B2", "C1"]

# 31 32 33 #data refrence
# 21 22 23
# 11 12 13


def getnums(text):
    # make a text string into a number string
    nums = ""
    for letter in text.upper():
        num = ord(letter) - 32
        if num < 10:
            num = "0" + str(num)
        nums = str(nums) + str(num)
    return int(nums)


def getext(nums):
    # make a number string into text string
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


def isopen(x, y, s=False):
    # get data about if a choordinit is open or not
    global cliii
    global clii
    global cli
    x, y = str(x), int(y)
    get = eval("cl" + ("i" * y) + "[" + str(ord(x) - 65) + "]")
    if not s:
        get = not bool(get)  # 0 = not false
    return get


def getpossibleplans():
    # get all possible plans, and add possible ones to list
    global pplans  # my possible plans
    global ppplans  # player's possible plans
    global plans  # all plans
    global CA
    global CB
    global CC
    global RA
    global RB
    global RC
    global DA
    global DB
    ppplans = []
    pplans = []
    for who in range(2):
        for p in plans:  # i = 'CA' or other
            posgood = 0
            for pos in eval(p):
                x, y = pos
                if isopen(x, y, True) in (0, (who + 1)):
                    posgood += 1
            if posgood == 3:
                if who:
                    ppplans.append(p)
                else:
                    pplans.append(p)


def chooseplan(who):
    # chose plan for user given in who
    global cliii
    global clii
    global cli
    global plan  # my curent plan
    global pplans  # my possible plans
    global ppplans  # player's possible plans
    global lpplan  # player's likely plan
    global custmove  # AI Custom Move var
    if who == 2:  # ai
        notwho = 1
        tovar = "plan"
        fromlist = "pplans"
        otherlist = "ppplans"
    else:  # player
        notwho = 2
        tovar = "lpplan"
        fromlist = "ppplans"
        otherlist = "pplans"
    # get stuff to choose from
    choosefrom = []
    data = []
    for p in eval(fromlist):  # for everything in possible plans
        for pos in eval(p):  # for each play in plan
            x, y = pos
            data.append(isopen(x, y, True))
            if data[len(data) - 1] == 0:  # if spot is playable
                choosefrom.append(p)  # add to choose from
    # start making stuff like Is player almost done with plan?
    almost = []
    for i in range(len(eval(fromlist))):  # for each possible plan,
        templist = tuple(
            data[(i * 3) : ((i + 1) * 3)]
        )  # get the data for that plan
        if (not (notwho in templist)) and (templist.count(who) > 1):
            almost.append(
                eval(fromlist)[i]
            )  # and if we have 2 moves and no other player plays
    if len(almost) > 0:
        for i in almost:  # make that thing more likely to play
            choosefrom.append(i)
            choosefrom.append(i)
    if isopen("B", 2):
        if who == 2:  # if B2's open, make it likely to choose it.
            for i in range(2):
                choosefrom.append("CM")
            custmove = "B2"
    if len(choosefrom) == 0:
        for p in eval(fromlist):  # i = plan
            for pos in eval(p):  # ii = play
                x, y = pos
                if isopen(x, y, True) is (0, who):
                    choosefrom.append(i)
    exec(tovar + " = " + choosefrom[random.randint(0, len(choosefrom) - 1)])


def planok(who):
    # check to ensure choosen plan is accualy possible to enact
    global CA
    global CB
    global CC
    global RA
    global RB
    global RC
    global DA
    global DB
    global custmove  # custom manuver (AI only)
    global plan  # my curent plan
    global lpplan  # player's likely plan
    if who == 2:
        dalist = "plan"
    else:
        dalist = "lpplan"
    toret = False
    if not eval(dalist) in ("CM", "NULL"):
        howmanyok = 0
        for i in eval(eval(dalist)):
            x, y = i
            if isopen(x, y):
                toret = True
                break
    elif who == 2:
        x, y = custmove
        toret = isopen(x, y)
    return toret


def emergencypickplan(who):
    # emergency pick a plan for who
    global CA
    global CB
    global CC
    global RA
    global RB
    global RC
    global DA
    global DB
    global plans
    global plan  # my curent plan
    global lpplan  # player's likely plan
    getpossibleplans()
    daplans = []
    for i in plans:  # CA, etc
        tmp = list(eval(i))  # ['A1', 'A2', 'A3'], etc.
        for ii in tmp:
            getemp = str(ii)  # A1
            xtmp = str(getemp[0])  # A
            ytmp = int(getemp[1])  # 1
            if isopen(xtmp, ytmp):
                daplans.append(i)
    if len(daplans) >= 1:
        choose = int(random.randint(0, len(daplans) - 1))
        if who == 2:
            plan = str(daplans[choose])
        else:
            lpplan = str(daplans[choose])
    elif len(pplans) >= 1:
        choose = int(random.randint(0, len(pplans) - 1))
        if who == 2:
            plan = str(pplans[choose])
        else:
            lpplan = str(pplans[choose])
    else:
        print("Developer Data Before Crash:")
        print(daplans)
        print(pplans)
        print(who)
        if who == 2:
            print(plan)
        else:
            print(lpplan)
        raise Exception("Not Sufficant Data to Choose From")


def chooseplay():
    # choose play AI will do
    global plan  # my curent plan
    global lpplan  # player's likely plan
    global CA
    global CB
    global CC
    global RA
    global RB
    global RC
    global DA
    global DB
    global ptofplay  # part of plan to play
    global custmove
    if not plan == "CM":
        tmp = int()
        # planpath = int(random.randint(7, 15)) #7/15 #5/14 = 4/9 primes
        planpath = int(random.randint(0, 8))
        if planpath <= 3:
            # against player play
            places = []
            pdat = []
            loc = []
            for i in eval(lpplan):
                x, y = i
                places.append(i)
                pdat.append(isopen(x, y, True))
            for i in range(len(pdat)):
                if int(pdat[i]) == 0:
                    loc.append(places[i])
        else:
            # self play
            loc = []
            for i in eval(plan):
                x, y = i
                if isopen(x, y):
                    loc.append(i)
        if len(loc) > 1:
            choose = random.randint(0, len(loc) - 1)
        else:
            choose = 0
        ptofplay = loc[choose]
    else:
        ptofplay = custmove


def aiturn():
    # were all da magic happens
    global plan
    global lpplan
    global ptofplay
    lpplan = "NULL"
    getpossibleplans()
    if not plan == "NULL":
        if not planok(2):
            chooseplan(2)
    else:
        chooseplan(2)
    chooseplan(1)
    if not planok(2):
        times = 0
        while not planok(2):
            chooseplan(2)
            times += 1
            if times > 3:
                emergencypickplan(2)
            if times > 5:
                try:
                    plan = plans[times - 5]
                except IndexError:
                    times = 0
                    print("AI: Resetting due to Error...")
                    reset()
    if not planok(1):
        times = 0
        while not planok(1):
            chooseplan(1)
            times += 1
            if times > 5:
                emergencypickplan(1)
            if times > 7:
                raise RuntimeError("AI: Attemted fix too many times")
    chooseplay()
    x, y = ptofplay
    if not isopen(x, y):
        while not isopen(x, y):
            print("AI: ERR: Play Not Ok")
            print("AI: MSG: Resetting Selected Play...")
            chooseplay()
            x, y = ptofplay
    return ptofplay


def play(pid, locx, locy):
    # play an X, O, or blank at a location.
    # pid = play ID, 2, 1, or 0, corspoding to O, X, and blank
    global cliii
    global clii
    global cli
    # program that plays moves
    wlist = str("cl" + ("i" * int(locx)))
    act = str(wlist + "[i]")
    for i in range(int(len(eval(wlist)))):
        part = str("pt" + ("i" * (i + 1)) + " = ")
        exec(str(part + str(eval(act))))
    part = str("pt" + ("i" * int(locy)))
    exec(str(part + " = " + str(pid)))
    for i in range(3):
        exec(str("del " + wlist + "[0]"))
    firstpt = str(wlist + ".append(")
    exec("global " + wlist)
    for i in range(3):
        part = str("pt" + ("i" * (i + 1)))
        exec(str(firstpt + part + ")"))


def update(data):
    # program that gets run to update data for the AI
    x, y, who = getext(data)
    play(who, x, y)


def turn():
    # program that accually gets the AI's play data and sends it to
    # the game
    data = aiturn()
    x, y = data
    x = ord(x) - 64
    play(2, y, x)
    return int(getnums(data))


def reset():
    # program that gets run to reset all data on the game board
    for i in range(3):
        for ii in range(3):
            play(0, int(i + 1), int(ii + 1))


def init():
    global plan
    global pplans
    plan = "NULL"
    pplans = []
    if registered:
        print("AI: This AI has been registered by Cat Ink.")
        print("to work with the Tic Tac Toe Game.")
    reset()


print("AI: AI Module Loaded")
print("AI: " + NAME + " Created by " + author)
