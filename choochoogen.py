#!/usr/bin/env python3

import random

ENGINES = ["🚂"]
CARS = ["🚃","🚋"]
SCENES = ["desert","forest","field","beach"]

ORBS = ["🌕","🌙","☀","☁"]
DESERT_TILES = ["🌵","🌵","🌴","🌴","🐪","🐢","🐎"]
FOREST_TILES = ["🌲","🌲","🌲","🌲","🐇","🌳","🌳"]
BEACH_TILES = ["🌴","🌴","🍍","🐢","🗿","🐚"]
FIELD_TILES = ["🌾","🌾","🌾","🌻","🐍","🐈"]
SEA_TILES =["🐬","🐳","🐙"]

HELL_TILES = ["🔥","👻","😈","💀"]
HEAVEN_TILES = ["📯👼","✨","🐕","👼"]
SPACE_TILES = ["👾","👽","💫","🚀","🛰"]
UNDERSEA_TILES = ["🐟","🐙","🐬","🐋"]

class Scene():
    def __init__(self, mode, height = 4, item_rarity = 10, top_border = None, bottom_border = None):
        self.mode = mode
        self.height = height
        self.item_rarity = item_rarity

        self.top_border = top_border
        self.bottom_border = bottom_border

        self.sky = ""
        self.landscape = []

        self.train = self.pick_engine() + self.pick_body()
    
    def pick_engine(self):
        leading_spaces = random.randint(0,9)
        self.engine = ""
        for _ in range(leading_spaces):
            self.engine += " "
        self.engine += random.choice(ENGINES)
        return self.engine

    def pick_body(self):
        self.body = ""
        cars = random.randint(3,8)
        for _ in range(cars):
            self.body += random.choice(CARS)
        return self.body
    
    def make_sky(self):
        self.sky = ""

        orb = random.choice(ORBS)
        orb_placement = random.randint(0,12)

        for _ in range(orb_placement):
            self.sky += u"\ua000"
        self.sky += orb
        
        return self.sky

    def make_sea(self):
        return self.fill_row(tileset = SEA_TILES, space_char = "🌊", length = 12)
     
    def fill_row(self, tileset = None, space_char = " ", length = 20):
        row = ""

        if not tileset:
            tileset = self.tileset
            
        for spot in range(length):
            tile = random.randint(1, self.item_rarity)
            if tile == 1:
                row += random.choice(tileset)
            else:
                row += space_char
        return row

    def generate(self):
        self.landscape = []

        if self.top_border:
            self.landscape.append(self.top_border)
        else:
            self.make_sky()
            self.landscape.append(self.fill_row())

        self.landscape.extend([self.fill_row(), self.fill_row()])

        if self.bottom_border:
            self.landscape.append(self.bottom_border)
        else:
            self.landscape.append(self.fill_row())

        if self.sky:
            print(self.sky)
            
        print(self.landscape[0], self.landscape[1], self.train, self.landscape[2], self.landscape[3], sep = '\n')

class Desert(Scene):
    def __init__(self):
        super(Desert, self).__init__("desert")
        self.tileset = DESERT_TILES

class Forest(Scene):
    def __init__(self):
        super(Forest, self).__init__("forest")
        self.tileset = FOREST_TILES

class Field(Scene):
    def __init__(self):
        super(Field, self).__init__("field")
        self.tileset = FIELD_TILES

class Space(Scene):
    def __init__(self):
        super(Space, self).__init__("space")
        self.top_border = "⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟"
        self.bottom_border = "⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟"
        
        self.tileset = SPACE_TILES

class Beach(Scene):
    def __init__(self):
        super(Beach, self).__init__("beach")
        self.tileset = BEACH_TILES
        self.bottom_border = self.make_sea()

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
    elif scene == "field":
        landscape, train = make_field()
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
# It appears most clients don't let tweets lead with whitespace.
# This commented out code would have put arbitrary whitespace in the sky
# But for now we'll just put the sun or moon or cloud on the far left
#    for _ in range(20):
#        sky += " "
#    orb_placement = random.randint(0,len(sky)-1)
#    sky = sky[:orb_placement] + orb + sky[orb_placement:]
    sky = orb
    return sky
    
if __name__ == "__main__":
    maketrain()
