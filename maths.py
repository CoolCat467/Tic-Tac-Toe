#!/usr/bin/env python3
# Maths Modual for Cat Inc Programs.
#
# Copywrite Cat Inc, All rights reserved.
# Programmed by CoolCat467, member of Cat Inc.

import os
global PRIMENUMBER
__version__ = '0.0.3'

def setPrime(number=2227501):
    global PRIMENUMBER
    PRIMENUMBER = int(number)

def getnums(text):
    # make a string into a number string
    nums = ''
    for letter in text.upper():
        num = ord(letter) - 32
        if num < 10:
            num = '0' + str(num)
        nums = str(nums) + str(num)
    return int(nums)

def getext(nums):
    # make a number string into text
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

def partquotes(text, witch, how = False):
    try:
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
    except SyntaxError:
        return 'Error'

def seperate(text):
    ftimes = 0
    scan = str(' ' + str(text))
    for i in scan:
        if str(i) == ' ':
            ftimes = ftimes + 1
            what = str('tmp' + str('i' * int(ftimes)))
            exec(str(what + " = ''"))
        else:
            what = str('tmp' + str('i' * int(ftimes)))
            tostore = str(eval(what) + str(i))
            if "'" in tostore:
                tostore = list(tostore)
                tmp = []
                for ii in tostore:
                    if "'" in str(ii):
                        tmp.append(str('\\\''))
                    else:
                        tmp.append(str(ii))
                tmp = str(''.join(tmp))
                tostore = tmp
            exec(str(what + " = '" + tostore + "'"))
    tmp = []
    for i in range(ftimes):
        what = str('tmp' + str('i' * int(i + 1)))
        tmp.append(str(eval(what)))
    return list(tmp)

def mkplain(word):
    tmp = []
    for i in range(26):
        tmp.append(chr(i + 65).lower())
    tmp.append("'")
    read = tuple(tmp)
    res = []
    for i in list(str(word).lower()):
        if i in read:
            res.append(chr(read.index(i) + 97))
            if res[len(res)-1] == '{':
                del res[len(res)-1]
                res.append("'")
    return str(''.join(res))

def timeCalc(totalsecs):
    # Calculate Time
    secs = int(totalsecs)
    mins = int((secs - (secs % 60)) / 60)
    secs = int(secs - (mins * 60))
    hrs  = int((mins - (mins % 60)) / 60)
    mins = int(mins - (hrs * 60))
    days = int((hrs - (hrs % 24)) / 24)
    hrs  = int(hrs - (days * 24))
    return tuple(str('%s\n%s\n%s\n%s' % (days, hrs, mins, secs)).splitlines())

def gethashed(text):
    # Take the entered text, hash it, and return it
    intstr = getnums(text)
    choose = 2
    data = ''
    intstr = int(intstr) * PRIMENUMBER
    for num in str(intstr):
        if choose % 2 != '0':
            data = str(data) + str(num)
        choose = choose + 1
    intstr = int(data) * PRIMENUMBER
    
    while len(str(intstr)) < 20:
        intstr = intstr * PRIMENUMBER
    if len(str(intstr)) > 20:
        choose = 0
        data = ''
        for i in str(intstr):
            choose = choose + 1
            if choose < 20:
                data = str(data) + str(i)
            else:
                data = int(data) * (int(i) + 1)
                #data = data
        intstr = int(data)
    return getext(intstr)

def hashfile(filename):
    data = []
    try:
        with open(filename, 'r') as readfile:
            for line in readfile:
                data.append(line)
            readfile.close()
    except FileNotFoundError:
        return 'Error'
    else:
        for i in range(len(data)):
            data.append(gethashed(str(data[0])))
            del data[0]
        data = str(''.join(data))
        data = str(gethashed(data))
        data = list(str(data))
        if ' ' in data or "'" in data or '"' in data:
            sel = 0
            for i in range(len(data) - 1):
                if data[sel] == ' ' or data[sel] == "'" or data[sel] == '"':
                    del data[sel]
                else:
                    sel += 1
        data = str(''.join(data))
        return data

def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

def RadixText(data):
    #Sorts text with RadixLSD
    try:
        cat = RadixLSD.__version__
    except NameError:
        contents = os.listdir(os.getcwd())
        if not 'RadixLSD.py' in contents:
            print('ERR: RadixLSD Modual is not present.')
            print('RadixText will not function without RadixLSD')
        else:
            import RadixLSD
    tosort = []
    for i in range(len(data)):
        tosort.append(mkplain(data[i]))
    tmp = ['']
    for i in range(26):
        tmp.append(chr(i + 65).lower())
    tmp.append("'")
    for i in range(10):
        tmp.append(i)
    tmp.append('')
    read = tuple(tmp)
    for i in tosort:
        tmp = []
        for ii in str(i).lower():
            try:
                dtmp = str(read.index(ii))
            except ValueError:
                dtmp = str(len(read)-1)
            if int(len(list(dtmp))%2) != 0:
                dtmp = str('0' + dtmp)
            tmp.append(dtmp)
        tosort[tuple(tosort).index(i)] = int(''.join(tmp))
    sort = RadixLSD.RadixLSD(tosort)
    for i in range(len(sort)):
        tmp = len(list(str(sort[i])))
        if bool(tmp % 2):
            sort[i] = str('0' + str(sort[i]))
        else:
            sort[i] = str(sort[i])
    for i in sort:
        tmp = []
        for ii in range(0, int(len(list(i))-1/2), 2):
            tmp.append(read[int(i[ii] + i[ii+1])])
        sort[tuple(sort).index(i)] = str(''.join(tmp))
    return sort

def seplist(readlist, sepby):
    #makes lists into text seperated by given values
    tmp = []
    for i in readlist:
        tmp.append(str(i))
        tmp.append(sepby)
    data = str(''.join(tmp))
    return data

def strlist(stredlist):
    #makes str()-ed lists back into true lists
    load = str(stredlist)
    l = partquotes(load, 1, how=True)
    tmp = []
    for i in range(l):
        tmp.append(partquotes(load, i+1))
    return tmp

def sysinfo():
    global SYSNAME
    global NODENAME
    global CURFOLD
    return tuple(str('%s\n%s\n%s' % (SYSNAME, NODENAME, CURFOLD)).splitlines()) 

def findwhole(percent, part):
    tmp = (part / (percent / 100))
    if int(tmp) == tmp:
        tmp = int(tmp)
    return tmp

def findpercent(part, whole):
    tmp = ((part / whole) * 100)
    if int(tmp) == tmp:
        tmp = int(tmp)
    return tmp

def findpart(percent, whole):
    tmp = (whole * (percent / 100))
    if int(tmp) == tmp:
        tmp = int(tmp)
    return tmp

def __init__():
    # Set some globals
    global SYSNAME
    global NODENAME
    global CURFOLD
    setPrime()
    SYSNAME = str(os.sys.platform.title())
    if os.name == 'posix':
        NODENAME = str(os.uname()[1])
    else:
        NODENAME = 'Unknown'
    CURFOLD = os.path.split(os.getcwd())[1]
    warnings()
    
def terminate():
    os.abort()
    exit()

def warnings():
    if sysinfo()[0] != 'Linux':
        print('WARNING: Some things may not work, as system is not Linux')

# Activation Program
__init__()
