#!/usr/bin/env python3
# Geometry Graphics Module

# Programmed by CoolCat467, member of Cat Inc.

__version__ = "0.0.0"

import math
import os
from tkinter import *

global tk
global canvas
global sprites


def init():
    global tk
    tk = Tk()


def window(windowname, width, height):
    global tk
    global canvas
    global WIDTH
    global HEIGHT
    init()
    tk.title(str(windowname))
    tk.resizable(0, 0)
    WIDTH = width
    HEIGHT = height
    # tk.wm_attributes('-topmost', 1)
    canvas = Canvas(tk, width=width, height=height, bd=0, highlightthickness=0)
    update()


def update():
    canvas.pack()
    canvas.update()


def clear(do=1):
    global sprites
    update()
    canvas.delete("all")
    if do == 2:
        sprites = []


def text(text, x, y, size=15, color="black", font="Times"):
    canvas.create_text(x, y, text=text, font=(font, size), fill=color)


def line(startx, starty, endx, endy, linewidth=5, color="black"):
    canvas.create_line(startx, starty, endx, endy, width=linewidth, fill=color)


def cross(x, y, r, w=5, c="black"):
    line(x - r, y - r, x + r, y + r, linewidth=w, color=c)
    line(x + r, y - r, x - r, y + r, linewidth=w, color=c)


def circle(x, y, radius, linewidth=5, color="black", outline=""):
    canvas.create_oval(
        x + radius,
        y + radius,
        x - radius,
        y - radius,
        width=linewidth,
        fill=color,
        outline=outline,
    )


def square(x, y, radius, linewidth=5, fillcolor="", outline="black"):
    xi = int(x - radius)
    yi = int(y - radius)
    xii = int(x + radius)
    yii = int(y + radius)
    canvas.create_rectangle(
        xi, yi, xii, yii, fill=fillcolor, outline=outline, width=linewidth
    )
    # canvas.create_polygon(xi, yii, xii, yii, xii, yi, xi, yi, fill=fillcolor, outline=outline, width=linewidth)


def rectangle(x, y, width, height, linewidth=5, fillcolor="", outline="black"):
    xi = int(x - int(width / 2))
    yi = int(y + int(height / 2))
    xii = int(x + int(width / 2))
    yii = int(y - int(height / 2))
    canvas.create_rectangle(
        xi, yi, xii, yii, fill=fillcolor, outline=outline, width=linewidth
    )


def pos(x, y, angle, distance):
    # get choords after move of distance at angle from given x and y
    theta_rad = (math.pi) / 2 - math.radians(angle)
    return x + distance * (math.cos(theta_rad)), y + distance * (
        math.sin(theta_rad)
    )


def polygon(
    x,
    y,
    radius,
    sides,
    offset=True,
    linewidth=5,
    fillcolor="",
    outline="black",
):
    if not sides > 126:
        angle = round(360 / int(sides))
        positions = []
        if str(type(offset)) == "<class 'bool'>":
            if offset:
                offset = 360 / (sides * 2)
        for i in range(int(sides)):
            positions.append(
                pos(x, y, round(angle * i + offset), round(radius / 2))
            )
        tmp = []
        for i in positions:
            for ii in i:
                tmp.append(str(round(ii)))
        tmp = str(tmp)
        tmp = str("".join(list(tmp)[1 : int(len(list(tmp)) - 1)]))
        arguments = str(
            tmp + ", fill=fillcolor, outline=outline, width=linewidth"
        )
        command = str("canvas.create_polygon(" + arguments + ")")
        exec(command)
    else:
        raise ValueError("Cannot draw shapes with more than 126 sides.")


class sprite:
    def __init__(self, name, x, y):
        self.name = str(name)
        self.x = x
        self.y = y
        self.color = "grey"
        self.border = ""
        self.linewidth = 5
        self.offset = True
        self.type = "square"
        # set all special to none
        self.diameter = None
        self.radius = 50
        self.width = None
        self.height = None
        self.sides = None
        self.procImm = False

    def medict(self):
        me = {
            "x": self.x,
            "y": self.y,
            "color": self.color,
            "border": self.border,
            "linewidth": self.linewidth,
            "offset": self.offset,
            "type": self.type,
            "diameter": self.diameter,
            "radius": self.radius,
            "size": self.size,
            "width": self.width,
            "height": self.height,
            "sides": self.sides,
        }
        return me

    def melist(self):
        me = [
            self.x,
            self.y,
            self.color,
            self.border,
            self.linewidth,
            self.offset,
            self.type,
            self.diameter,
            self.radius,
            self.size,
            self.width,
            self.height,
            self.sides,
        ]
        return me

    def __str__(self):
        me = []
        for i in self.melist():
            me.append(str(i) + ", ")
        me = list(str("".join(me)))
        me = str("".join(me[0 : len(me) - 2]))
        return me

    def circle(self, diameter):
        self.type = "circle"
        self.diameter = int(diameter)
        if self.procImm:
            self.proc()

    def square(self, size):
        self.type = "square"
        self.radius = int(size * 2)
        if self.procImm:
            self.proc()

    def rect(self, width, height):
        self.type = "rect"
        self.width, self.height = int(width), int(height)
        if self.procImm:
            self.proc()

    def polygon(self, sides, radius):
        self.type = "poly"
        self.sides, self.radius = int(sides), int(radius)
        if self.procImm:
            self.proc()

    def move(self, angle, distance):
        self.x, self.y = pos(self.x, self.y, angle, distance)
        if self.procImm:
            self.proc()

    def proc(self):
        global custCommands
        for i in custCommands:
            cmds.append(str(i[0]))
        if self.type == "square":
            save = (
                self.name,
                self.type,
                self.x,
                self.y,
                self.radius,
                self.linewidth,
                self.color,
                self.border,
            )
        elif self.type == "rect":
            save = (
                self.name,
                self.type,
                self.x,
                self.y,
                self.width,
                self.height,
                self.linewidth,
                self.color,
                self.border,
            )
        elif self.type == "poly":
            save = (
                self.name,
                self.type,
                self.x,
                self.y,
                self.radius,
                self.sides,
                self.offset,
                self.linewidth,
                self.color,
                self.border,
            )
        elif self.type == "circle":
            save = (
                self.name,
                self.type,
                self.x,
                self.y,
                self.radius,
                self.linewidth,
                self.color,
                self.border,
            )
        elif self.type in cmds:
            save = custCmdHandleing(self.medict())
        else:
            raise TypeError("Type Invalid")
        self.update(save)

    def update(self, data):
        global sprites
        tmpsprites = []
        for i in sprites:
            if i[0] != self.name:
                tmpsprites.append(i)
        tmpsprites.append(data)
        sprites = tmpsprites

    def printall(self):
        for i in range(len(list(self.medict().values()))):
            print(
                list(self.medict().keys())[i]
                + " = "
                + list(self.medict().values())[i]
            )

    pass


def addCustDraw(name, program, handleprog):
    global drawCommands
    custCommands.append(tuple(str(name), str(program), str(handleprog)))


def custCmdHandleing(dictin):
    global custCommands
    names = []
    hndlProg = []
    for i in custCommands:
        names.append(i[0])
        hndlProg.append(i[2])
    names = tuple(names)
    if str(dictin["type"]) in names:
        prog = hndlProg[names.index(str(dictin["type"]))]
        exec(prog + "(" + dictin + ")")


def drawSprites():
    conv = {
        "square": "square",
        "rect": "rectangle",
        "poly": "polygon",
        "circle": "circle",
    }
    global sprites
    global custCommands
    names = []
    programs = []
    spritenames = []
    for i in custCommands:
        names.append(str(i[0]))
        programs.append(str(i[1]))
    names, programs = tuple(names), tuple(programs)
    for i in sprites:
        # establish name and drawing handleing
        spritenames.append(i[0])
        tmp = str(i[1])
        if tmp in list(conv.keys()):
            prefix = conv[tmp]
        elif tmp in names:
            prefix = program[names.index(tmp)]
        else:
            command = str(tmp)
            spritename = str(i[0])
            raise LookupError(
                'Command "%s" Not Found in Sprite "%s"' % (command, spritename)
            )
        # argument
        argz = str(i[2 : len(i)])
        exec(prefix + argz)
    return tuple(spritenames)


def __init__():
    # Set some globals
    global SYSNAME
    global NODENAME
    global CURFOLD
    SYSNAME = str(os.sys.platform.title())
    if os.name == "posix":
        NODENAME = str(os.uname()[1])
    else:
        NODENAME = "Unknown"
    CURFOLD = os.path.split(os.getcwd())[1]
    global sprites
    sprites = []
    global custCommands
    custCommands = {}
    warnings()
    test()


def terminate():
    os.abort()
    exit()


def test():
    global cat
    window("Test Window", 500, 500)
    cat = sprite("Cat", 250, 250)
    cat.polygon(8, 200)
    cat.border = "black"
    cat.color = "red"
    cat.proc()
    drawSprites()


def warnings():
    global SYSNAME
    if SYSNAME != "Linux":
        print("WARNING: Some things may not work, as system is not Linux")


# Activation Program
__init__()
