#!/usr/bin/env python3

import random

ENGINES = ["🚂"]
CARS = ["🚃","🚋"]
SCENES = ["desert","forest"]

ORBS = ["🌕","🌙","☀","☁"]
DESERT_TILES = ["🌵","🌵","🐪","🐢","🐎",""]
FOREST_TILES = ["🌲","🌲","🌲","🐇","🌳"]

def maketrain():
    engine = pick_engine()
    body = pick_body()
    train = engine + body
    landscape = make_landscape()
    sky = make_sky()
    mise_en_scene = (
    sky + "\n" + \
    landscape[0] + "\n" + \
    landscape[1] + "\n" + \
    train + "\n" + \
    landscape[2] + "\n" + \
    landscape[3])
    return mise_en_scene

def make_landscape():
    landscape = []
    scene = random.choice(SCENES)
    if scene == "desert":
        tileset = DESERT_TILES
    elif scene == "forest":
        tileset = FOREST_TILES
    for row in range(4):
        row = ""
        for spot in range(20):
            tile = random.randint(0,100)
            if tile%10 == 0:
                row += random.choice(tileset)
            else:
                row += " "
                
        landscape.append(row)
    return landscape    

def make_sky():
    sky = ""
    orb = random.choice(ORBS)
    for _ in range(20):
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
    cars = random.randint(1,10)
    for _ in range(cars):
        body += random.choice(CARS)
    return body

if __name__ == "__main__":
    maketrain()
