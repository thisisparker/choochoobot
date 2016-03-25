#!/usr/bin/env python3

import random

ENGINES = ["🚂"]
CARS = ["🚃","🚋"]
SCENES = ["desert","forest","beach"]

ORBS = ["🌕","🌙","☀","☁"]
DESERT_TILES = ["🌵","🌵","🌴","🌴","🐪","🐢","🐎"]
FOREST_TILES = ["🌲","🌲","🌲","🌲","🐇","🌳","🌳"]
BEACH_TILES = ["🌴","🌴","🍍","🐢","🗿","🐚"]
SEA_TILES =["🐬","🐳","🐙"]

HELL_TILES = ["🔥","👻","😈","💀"]
HEAVEN_TILES = ["📯👼","✨","🐕","👼"]
SPACE_TILES = ["👾","👽","💫","🚀","🛰"]
UNDERSEA_TILES = ["🐟","🐙","🐬","🐋"]

def maketrain():
    scene = random.choice(SCENES)
    if random.randint(1,12) == 12:
        scene = "special"
    sky = make_sky()
    if scene == "desert":
        landscape, train = make_desert()
    elif scene == "forest":
        landscape, train = make_forest()
    elif scene == "beach":
        landscape, train = make_beach()
    elif scene == "special":
        sky = ""
        landscape, train = make_special()
    mise_en_scene = (
    sky + "\n" + \
    landscape[0] + "\n" + \
    landscape[1] + "\n" + \
    train + "\n" + \
    landscape[2] + "\n" + \
    landscape[3])
    return mise_en_scene 

def make_desert():
    train = pick_engine() + pick_body()
    landscape = []
    tileset = DESERT_TILES
    for row in range(4):
        row = ""
        for spot in range(20):
            tile = random.randint(0,1000)
            if tile%10 == 0:
                row += random.choice(tileset)
            else:
                row += " "
        landscape.append(row)
    return landscape, train

def make_forest():
    train = pick_engine() + pick_body()
    landscape = []
    tileset = FOREST_TILES
    for row in range(4):
        row = ""
        for spot in range(20):
            tile = random.randint(0,1000)
            if tile%10 == 0:
                row += random.choice(tileset)
            else:
                row += " "
        landscape.append(row)
    return landscape, train

def make_beach():
    train = pick_engine() + pick_body()
    landscape = []
    tileset = BEACH_TILES
    for row in range(3):
        row = ""
        for spot in range(20):
            tile = random.randint(0,1000)
            if tile%10 == 0:
                row += random.choice(tileset)
            else:
                row += " "
        landscape.append(row)
    tileset = SEA_TILES
    lastrow = ""
    for spot in range(12):
        tile = random.randint(0,1000)
        if tile%10 == 0:
            lastrow += random.choice(tileset)
        else:
            lastrow += "🌊"
    landscape.append(lastrow)
    return landscape, train

def make_special():
    train = pick_engine() + pick_body()

    scene = random.choice(["hell","heaven","space","undersea"])
    if scene == "hell":
        border = "🔥👹🔥👹🔥👹🔥👹🔥👹🔥👹"
        tileset = HELL_TILES
    elif scene == "heaven":
        border = "☁👼☁👼☁👼☁👼☁👼☁👼"
        tileset = HEAVEN_TILES
    elif scene == "space":
        border = "⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟"
        tileset = SPACE_TILES
    elif scene == "undersea":
        border = "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊"
        tileset = UNDERSEA_TILES
    landscape = [border]
    for row in range(2):
        row = ""
        for spot in range(20):
            tile = random.randint(0,1000)
            if tile%10 == 0:
                row += random.choice(tileset)
            else:
                row += " "
        landscape.append(row)
    landscape.append(border)

    return landscape, train

def make_sky():
    sky = ""
    orb = random.choice(ORBS)

    for _ in range(19):
            tile = random.randint(0,1000)
            if tile%10 == 0:
                sky += "☁"
            else:
                sky += " "

    orb_placement = random.randint(0,len(sky)-1)
    sky = sky[:orb_placement] + orb + sky[orb_placement:]

    return sky
    

def pick_engine():
    leading_spaces = random.randint(0,9)
    engine = ""
    for _ in range(leading_spaces):
        engine += " "
    engine += random.choice(ENGINES)
    return engine

def pick_body():
    body = ""
    cars = random.randint(1,8)
    for _ in range(cars):
        body += random.choice(CARS)
    # body += "💨"
    return body

if __name__ == "__main__":
    maketrain()
