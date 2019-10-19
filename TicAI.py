#!/usr/bin/env python
# AI that plays tic tac toe.
#
# Copywrite Cat Inc, All rights reserved.
# Programmed by Samuel Davenport, member of Cat Inc.
#
# isPrime Thanks to Anivargi's Twin prime calculator at
# Scratch.mit.edu/projects/128640110/ for the program that
# finds out if it is prime or not.
#
# Import os for several important stuff
# Import sys for sys.exit function
# Import time for time.time() function
# Import math for square root function
# Import random's radint for random intigers

import os, sys, time, math
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
global ptofplay #part of plan to play
global custmove #custom move data (set with plan = 'CM')
cliii = [0, 0, 0] #ai's equivelent to liii
clii = [0, 0, 0] #ai's equivelent to lii
cli = [0, 0, 0] #ai's equivelent to li
pplans = [] #ai possible plans
plan = '' #ai current plan
ppplans = [] #player's possible plans
lpplan = '' #player's likely plan
plans = ['CA', 'CB', 'CC', 'RA', 'RB', 'RC', 'DA', 'DB'] #All Plans
CA = ['A1', 'A2', 'A3']
CB = ['B1', 'B2', 'B3']
CC = ['C1', 'C2', 'C3']
RA = ['A1', 'B1', 'C1']
RB = ['A2', 'B2', 'C2']
RC = ['A3', 'B3', 'C3']
DA = ['A1', 'B2', 'C3']
DB = ['A3', 'B2', 'C1']

# 31 32 33 #data refrence
# 21 22 23
# 11 12 13

def isPrime(num):
    # Anivargi's program that finds out if it is prime or not. See top
    isPrime = True
    if num < 3 or num == 3:
        isPrime = True
    else:
        divideNumber = 2
        while isPrime == True and divideNumber != math.ceil(math.sqrt(num + 1)):
            if num % divideNumber == 0:
                isPrime = False
            else:
                divideNumber = divideNumber + 1
    return isPrime

def getnums(text):
    # make a text string into a number string
    nums = ''
    for letter in text.upper():
        num = ord(letter) - 32
        if num < 10:
            num = '0' + str(num)
        nums = str(nums) + str(num)
    return int(nums)

def getext(nums):
    # make a number string into text string
    control = 1
    prev = ''
    text = ''
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
            if num == '0':
                text = text + ' '
            else:
                text = text + chr(int(num) + 32)
            control = 1
    return text

def partquotes(text, witch, how=False):
    '''takes input, like "I think 'cats' are so 'cool' yay",
    in input text, which defines which part im quotes
    of 'cats' and 'cool' gets returned. if how is set True,
    it takes text input, which is ignored, and it returns
    howmany parts are in quotes in the text.'''
    ftimes = 0
    found = False
    for i in text:
        if not found:
            if i == "'":
                found = True
                ftimes = ftimes + 1
                var = 'l' + str('i' * ftimes)
                exec("%s = ''" % var)
                to = "%s = %s + " % (var, var)
        else:
            if i != "'":
                exec(str(to) + "'" + i + "'")
            else:
                found = False
    var = 'l' + str('i' * int(witch))
    if not how:
        toreturn = eval(var)
    else:
        toreturn = ftimes
    return toreturn

def getCordInf(x, y):
    #return data about the given playing choordinits
    global cliii
    global clii
    global cli
    wlist = str('cl' + ('i' * int(y)))
    act = str(wlist + '[' + str(int(x) - 1) + ']')
    return int(eval(act))

def mkplaysynax(xpos):
    #takes num, 1-3, and returns A-C
    retx = str(chr(int(xpos) + 64))
    return retx

def mknumsynax(xpos):
    #takes letter, A-C, and returns 1-3
    retx = str(ord(xpos) - 64)
    return retx

def isopen(x, y, s=False):
    #same as getChordInf, but seems to work better
    global cliii
    global clii
    global cli
    xpos = int(mknumsynax(x))
    get = int(getCordInf(xpos, int(y)))
    if s:
        toret = get
    else:
        if get == 0:
            toret = True
        else:
            toret = False
    return toret

def getpossibleplans():
    #get all possible plans, and add possible ones to user's list
    global cliii
    global clii
    global cli
    global plan #my curent plan
    global pplans #my possible plans
    global ppplans #player's possible plans
    global lpplan #player's likely plan
    global plans # all plans
    global CA
    global CB
    global CC
    global RA
    global RB
    global RC
    global DA
    global DB
    for iii in range(2):
        if int(iii) == 1:
            addlist = 'ppplans'
            menum = 1
        else:
            addlist = 'pplans'
            menum = 2
        #Start of code to 
        act = str('del ' + addlist + '[0]')
        for i in range(int(len(eval(addlist)))):
            exec(act) #Clear all pre-existing data
        for i in plans: #i = 'CA' or other
            tmp = list(eval(i)) #tmp = ['A1', 'A2', 'A3']
            ltmp = 0
            for ii in range(3):
                getemp = str(tmp[ii]) # A1
                xtmp = str(getemp[0]) #A
                ytmp = int(getemp[1]) #1
                dtmp = isopen(xtmp, ytmp, True)
                if dtmp == 0 or dtmp == menum:
                    ltmp = int(ltmp + 1)
            if ltmp == 3:
                exec(str(addlist + ".append('" + i + "')"))

def chooseplan(who):
    #chose plan for user given in who
    global cliii
    global clii
    global cli
    global plan #my curent plan
    global pplans #my possible plans
    global ppplans #player's possible plans
    global lpplan #player's likely plan
    global custmove #AI Custom Move var
    if who == 2:
        tovar = 'plan'
        fromlist = 'pplans'
        otherlist = 'ppplans'
    else:
        tovar = 'lpplan'
        fromlist = 'ppplans'
        otherlist = 'pplans'
    #get stuff to choose from
    choosefrom = []
    data = []
    for i in list(eval(fromlist)): #i = plan
        for ii in eval(i): #ii = play
            x = str(ii[0])
            y = int(ii[1])
            dtmp = int(isopen(x, y, True))
            data.append(dtmp)
            if dtmp == 0:
                choosefrom.append(i)
    #start making stuff like Is player almost done with plan?
    almost = []
    #make conditions
    cond = 'data[sel] == who or data[sel] == 0'
    for i in range(len(eval(fromlist))):
        #choosefrom.append(eval(fromlist)[i]) #removed cuz makes it dummer
        for ii in range(3):
            sel = int(ii)
            do = str('tmp' + str('i' * sel) + ' = eval(cond)')
            exec(do)
        do = ''
        for ii in range(3):
            do = do + str('tmp' + str('i' * int(ii)) + ' and ')
        do = do + 'True'
        #finaly see if built condition is True
        if eval(do):
            almost.append(eval(fromlist)[i])
            #if is, put in in almost
    if len(almost) > 0:
        for i in almost:
            choosefrom.append(i)
            choosefrom.append(i)
            # if it's in almost, make more likely to pick that
    if isopen('B', 2):
        if who == 2: #if B2's open, make it likely to choose it.
            for i in range(3):
                choosefrom.append('CM')
            custmove = 'B2'
    if len(choosefrom) > 1: #random choose plan
        choosen = int(random.randint(0, int(len(choosefrom)) - 1))
    else:
        choosen = 0
    if choosen > len(choosefrom):
        choosen = len(choosefrom) - 1
    try:
        pick = str(choosefrom[choosen])
    except IndexError:
        for i in list(eval(fromlist)): #i = plan
            for ii in eval(i): #ii = play
                x = str(ii[0])
                y = int(ii[1])
                dtmp = int(isopen(x, y, True))
                choosefrom.append(i)
            choosen = int(random.randint(0, int(len(choosefrom)) - 1))
            pick = str(choosefrom[choosen])
    else:   
        do = str(tovar + " = '" + pick + "'")
        if tovar == 'plan':
            plan = pick
        elif tovar == 'lpplan':
            lpplan = pick
        else:
            raise NameError('Name of var to store to not given')
        
def planok(who):
    #bug checker to ensure choosen plan is accualy possible
    global CA
    global CB
    global CC
    global RA
    global RB
    global RC
    global DA
    global DB
    global custmove #custom manuver (AI only)
    global plan #my curent plan
    global lpplan #player's likely plan
    if who == 2:
        dalist = 'plan'
    else:
        dalist = 'lpplan'
    if not eval(dalist) == 'CM':
        howmanyok = 0
        litmp = eval(dalist) #i = 'CA' or other
        tmp = list(eval(litmp)) #tmp = ['A1', 'A2', 'A3']
        ltmp = 0
        for ii in range(3):
            getemp = str(tmp[ii]) # A1
            xtmp = str(getemp[0]) #A
            ytmp = int(getemp[1]) #1
            dtmp = isopen(xtmp, ytmp)
            if dtmp:
                ltmp = int(ltmp + 1)
            if ltmp >= 1:
                howmanyok = howmanyok + 1
        if howmanyok >= 1:
            toret = True
        else:
            toret = False
    elif who == 2:
        getemp = str(custmove) # A1
        xtmp = str(getemp[0]) #A
        ytmp = int(getemp[1]) #1
        if isopen(xtmp, ytmp):
            toret = True
        else:
            toret = False
    else:
        toret = False
    return toret

def emergencypickplan(who):
    #emergency pick a plan for who
    global CA
    global CB
    global CC
    global RA
    global RB
    global RC
    global DA
    global DB
    global plans
    global plan #my curent plan
    global lpplan #player's likely plan
    getpossibleplans()
    daplans = []
    for i in plans: #CA, etc
        tmp = list(eval(i)) #['A1', 'A2', 'A3'], etc.
        for ii in tmp:
            getemp = str(ii) # A1
            xtmp = str(getemp[0]) #A
            ytmp = int(getemp[1]) #1
            if isopen(xtmp, ytmp):
                daplans.append(i)
    if len(daplans) >= 1:
        choose = int(random.randint(0, len(daplans) - 1))
        if who == 2:
            plan = str(daplans[choose])
        else:
            lpplan = str(dapland[choose])
    else:
        print('Devel')
        print(pplans)
        if who == 2:
            print(plan)
        else:
            print(lpplan)
        raise Exception('Not Sufficant Data to Choose From')

def chooseplay():
    #choose play AI will do
    global plan #my curent plan
    global lpplan #player's likely plan
    global CA
    global CB
    global CC
    global RA
    global RB
    global RC
    global DA
    global DB
    global ptofplay #part of plan to play
    global custmove
    if not plan == 'CM':
        tmp = int()
        planpath = int(random.randint(7, 15)) #7/15 #5/14 = 4/9
        if isPrime(planpath):
            #against player play
            places = []
            pdat = []
            loc = []
            for i in eval(lpplan):
                xtmp = str(i[0]) #A
                ytmp = int(i[1]) #1
                places.append(i)
                pdat.append(isopen(xtmp, ytmp, True))
            for i in range(len(pdat)):
                if int(pdat[i]) == 0:
                    loc.append(places[i])
        else:
            #self play
            loc = []
            for i in eval(plan):
                xtmp = str(i[0]) #A
                ytmp = int(i[1]) #1
                if isopen(xtmp, ytmp):
                    loc.append(i)
        if len(loc) > 1:
            choose = int(random.randint(0, len(loc) - 1))
        else:
            choose = 0
        ptofplay = str(loc[choose])
    else:
        ptofplay = custmove

def playok():
    #checks to ensure play choosen is possible to play at
    global ptofplay
    xtmp = str(ptofplay[0]) #A
    ytmp = int(ptofplay[1]) #1
    if isopen(xtmp, ytmp):
        toret = True
    else:
        toret = False
    return toret

def getdata(mode):
    #return turn information
    global ptofplay #part of plan to play
    data = str(ptofplay)
    if str(mode) == 'X':
        toret = str(data[0])
    else:
        toret = int(data[1])
    return toret

def aiturn():
    #were all da magic happens
    global plan
    global lpplan
    lpplan = 'NULL'
    getpossibleplans()
    if not plan == 'NULL':
        if not planok(2):
            chooseplan(2)
    else:
        chooseplan(2)
    chooseplan(1)
    ok = planok(2)
    if not ok:
        times = 0
        while not ok:
            getpossibleplans()
            chooseplan(2)
            times = times + 1
            if times > 3:
                emergencypickplan(2)
            if times > 5:
                try:
                    plan = plans[times - 5]
                except IndexError:
                    times = 0
                    print('Uh oh...')
                    reset()
            ok = planok(2)
            time.sleep(0.3)
    ok = planok(1)
    if not ok:
        times = 0
        while not ok:
            getpossibleplans()
            chooseplan(1)
            times = times + 1
            if times > 5:
                emergencypickplan(1)
            if times > 7:
                raise RuntimeError('Attemted fix too manny times')
            ok = planok(1)
            time.sleep(0.3)
    chooseplay()
    ok = playok()
    if not ok:
        while not ok:
            time.sleep(1)
            print('AI: ERR: Play Not Ok')
            print('AI: MSG: Resetting Selected Play...')
            chooseplay()
            ok = playok()
    x = getdata('X')
    y = getdata('Y')
    toret = str(str(x) + str(y))
    return int(getnums(toret))

def play(pid, locx, locy):
    #play an X, O, or blank at a location.
    #pid = play ID, 2, 1, or 0, corspoding to O, X, and blank
    global cliii
    global clii
    global cli
    # program that plays moves
    wlist = str('cl' + ('i' * int(locx)))
    act = str(wlist + '[i]')
    for i in range(int(len(eval(wlist)))):
        part = str('pt' + ('i' * (i + 1)) + ' = ')
        exec(str(part + str(eval(act))))
    part = str('pt' + ('i' * int(locy)))
    exec(str(part + ' = ' + str(pid)))
    for i in range(3):
        exec(str('del ' + wlist + '[0]'))
    firstpt = str(wlist + '.append(')
    exec('global ' + wlist)
    for i in range(3):
        part = str('pt' + ('i' * (i + 1)))
        exec(str(firstpt + part + ')'))
    toret = True
    return toret

def update(data):
    #program that gets run to update data for the AI
    decdata = str(getext(data))
    x = int(decdata[0])
    y = int(decdata[1])
    who = int(decdata[2])
    return play(who, x, y)

class mini:
    def start(self):
        while True:
            try:
                time.sleep(0.01)
            except KeyboardInterrupt:
                print('Devel')
                print(lpplan)
            else:
                time.sleep(0.01)
    pass

def turn():
    #program that accually gets the AI's play data and sends it to
    #the game
    data = aiturn()
    decdata = str(getext(data))
    posy = int(decdata[1])
    posx = mknumsynax(str(decdata[0]))
    temp = play(2, posy, posx)
    return data

def reset():
    #program that gets run to reset all data on the game board
    for i in range(3):
        for ii in range(3):
            play(0, int(i + 1), int(ii + 1))

def start():
    global plan
    global pplans
    plan = 'NULL'
    pplans = []
    print('AI Created by Samuel Davenport')
    print('This has been registered by Cat Inc.')
    print('to work with the Tic Tac Toe API.')
    reset()

print('AI Module Loaded')
print('AI Created by Samuel Davenport')
