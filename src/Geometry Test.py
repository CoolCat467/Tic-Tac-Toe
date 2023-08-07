#!/usr/bin/env python3
# Test of the Geometry Graphics Module
# Created by CoolCat467

import random
import time

import geometry as geo

__version__ = "0.0.0"
SIZE = 500
HALF = int(SIZE / 2)


def init():
    geo.window("Geometry Grapics Module Test", SIZE, SIZE)
    geo.update()


def loading(x, y, size, rotangle=12, runtime=60, speed=0.003, linewidth=3):
    try:
        x, y, size, rotangle, speed = (
            round(x),
            round(y),
            round(size),
            round(rotangle),
            float(speed),
        )
        times = round(runtime / (284 * speed) + (runtime / (9783 * speed)))
        for merp in range(times):
            for i in range(int(180 / rotangle), 0, -1):
                geo.circle(
                    x,
                    y,
                    size,
                    linewidth=linewidth,
                    color="white",
                    outline="black",
                )
                for ii in range(90):
                    geo.polygon(
                        x,
                        y,
                        int(size * 2),
                        2,
                        offset=0 - (ii + ((i + 1) * rotangle)),
                        linewidth=linewidth,
                        fillcolor="black",
                    )
                geo.update()
                time.sleep(speed)
                geo.clear()
    except KeyboardInterrupt:
        print("Done")


def penta():
    colors = ("red", "blue", "green", "orange", "purple", "white", "black")
    while True:
        geo.clear()
        for i in range(50):
            color = colors[random.randint(0, 6)]
            move = int(random.randint(0, 359))
            size = int(random.randint(10, 400))
            shape = int(random.randint(1, 10))
            geo.polygon(HALF, HALF, size, shape, offset=move, fillcolor=color)
            geo.update()
            time.sleep(0.1)


if __name__ == "__main__":
    init()
    # penta()
    loading(250, 250, 8, linewidth=1)
