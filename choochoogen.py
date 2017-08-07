#!/usr/bin/env python3

import random
from datetime import datetime, timedelta
import pytz
import astral
import xml.etree.ElementTree as ET
import requests

ENGINES = ["🚂"]
CARS = ["🚃","🚋"]

SUN = "☀"
MOONS = ["🌑","🌒","🌔","🌕","🌘","🌖"]
DESERT_TILES = ["🌵","🌵","🌴","🌴","🐪","🐢","🐎"]
FOREST_TILES = ["🌲","🌲","🌲","🌲","🐇","🌳","🌳"]
BEACH_TILES = ["🌴","🌴","🍍","🐢","🗿","🐚"]
FIELD_TILES = ["🌾","🌾","🌾","🌻","🐍","🐈"]
WILDFLOWERS_TILES = ["🌼","🌺","🏵️","🌷","🌷","🐝","🦋"]
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

    def get_weather(self):
        cloud_terms = ["Mostly Cloudy", "Mostly Cloudy with Haze", "Mostly Cloudy and Breezy", "A Few Clouds", "A Few Clouds with Haze", "A Few Clouds and Breezy", "Partly Cloudy", "Partly Cloudy with Haze", "Partly Cloudy and Breezy", "Overcast", "Overcast with Haze", "Overcast and Breezy", "Fog/Mist", "Fog", "Freezing Fog", "Shallow Fog", "Partial Fog", "Patches of Fog", "Fog in Vicinity", "Freezing Fog in Vicinity", "Shallow Fog in Vicinity", "Partial Fog in Vicinity", "Patches of Fog in Vicinity", "Showers in Vicinity Fog", "Light Freezing Fog", "Heavy Freezing Fog"]
        rain_terms = ["Rain Showers", "Light Rain Showers", "Light Rain and Breezy", "Heavy Rain Showers", "Rain Showers in Vicinity", "Light Showers Rain", "Heavy Showers Rain", "Showers Rain", "Showers Rain in Vicinity", "Rain Showers Fog/Mist", "Light Rain Showers Fog/Mist", "Heavy Rain Showers Fog/Mist", "Rain Showers in Vicinity Fog/Mist", "Light Showers Rain Fog/Mist", "Heavy Showers Rain Fog/Mist", "Showers Rain Fog/Mist", "Showers Rain in Vicinity Fog/Mist", "Light Rain", "Drizzle", "Light Drizzle", "Heavy Drizzle", "Light Rain Fog/Mist", "Drizzle Fog/Mist", "Light Drizzle Fog/Mist", "Heavy Drizzle Fog/Mist", "Light Rain Fog", "Drizzle Fog", "Light Drizzle Fog", "Heavy Drizzle Fog Rain", "Heavy Rain", "Rain Fog/Mist", "Heavy Rain Fog/Mist", "Rain Fog", "Heavy Rain Fog"]
        
        try:
            res = requests.get("http://w1.weather.gov/xml/current_obs/KJRB.xml")
            xml_tree = ET.fromstring(res.text)
            weather = xml_tree.find('weather').text

            if weather in cloud_terms:
                self.sky = self.fill_row(tileset = ["☁️"])
                return self.sky
            elif weather in rain_terms:
                self.sky = self.fill_row(tileset = ["🌧️,🌧️,☁️"])
            elif "Thunderstorm" in weather:
                self.sky = self.fill_row(tileset = ["🌧️","⛈️","⛈️"])
            elif "Snow" in weather:
                self.sky = self.fill_row(tileset = ["🌨️","❄️"])
            else:
                return None
        except:
            return None

    def make_daysky(self):
        day_length = self.loc.sunset() - self.loc.sunrise()
        day_so_far = self.dt - self.loc.sunrise()

        sun_placement = int((day_so_far.seconds/day_length.seconds) * 12)

        for _ in range(sun_placement):
            self.sky += u"\u2800"
        self.sky += SUN + u"\uFE0F"
 
    def make_nightsky(self):
        a = astral.Astral()
        moon_phase = a.moon_phase(self.dt.date())

        if moon_phase == 0:
            moon = MOONS[0] 
        elif moon_phase < 7:
            moon = MOONS[1]
        elif moon_phase < 14:
            moon = MOONS[2]
        elif moon_phase == 14:
            moon = MOONS[3]
        elif moon_phase < 21:
            moon = MOONS[4]
        else:
            moon = MOONS[5]

        if self.dt > self.loc.sunset():
            tomorrow = self.dt + timedelta(days = 1)
            night_length = self.loc.sunrise(tomorrow) - self.loc.sunset()
            night_so_far = self.dt - self.loc.sunset()
        elif self.dt < self.loc.sunrise():
            yesterday = self.dt - timedelta(days = 1)
            night_length = self.loc.sunrise() - self.loc.sunset(yesterday)
            night_so_far = self.dt - self.loc.sunset(yesterday)

        moon_placement = int((night_so_far.seconds/night_length.seconds) * 12)

        for _ in range(moon_placement):
            self.sky += u"\u2800"
        self.sky += moon + u"\uFE0F"

    def make_sky(self):
        self.sky = ""
        
        self.dt = pytz.timezone('America/New_York').localize(datetime.now())
        self.loc = astral.Location(("New York","New York", 40.7527, -73.9772,"America/New_York","0"))

        if self.dt >= self.loc.sunrise() and self.dt <= self.loc.sunset():
            self.weather = self.get_weather()
            if not self.weather:
                self.make_daysky()
        else:
            self.make_nightsky()
       
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

        tweet = ""
        if self.sky:
            tweet += self.sky + "\n"
            
        tweet += self.landscape[0] + "\n" + \
                 self.landscape[1] + "\n" + \
                 self.train + "\n" + \
                 self.landscape[2] + "\n" + \
                 self.landscape[3]

        return tweet

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

class Wildflowers(Scene):
    def __init__(self):
        super(Wildflowers, self).__init__("wildflowers")
        self.tileset = WILDFLOWERS_TILES

class Beach(Scene):
    def __init__(self):
        super(Beach, self).__init__("beach")
        self.tileset = BEACH_TILES
        self.bottom_border = self.make_sea()

class Space(Scene):
    def __init__(self):
        super(Space, self).__init__("space")
        self.top_border = "⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟"
        self.bottom_border = "⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟⭐🌟"
        self.tileset = SPACE_TILES

class Hell(Scene):
    def __init__(self):
        super(Hell, self).__init__("hell")
        self.top_border = "🔥👹🔥👹🔥👹🔥👹🔥👹🔥👹"
        self.bottom_border = "🔥👹🔥👹🔥👹🔥👹🔥👹🔥👹"
        self.tileset = HELL_TILES

class Heaven(Scene):
    def __init__(self):
        super(Heaven, self).__init__("heaven")
        self.top_border = "☁👼☁👼☁👼☁👼☁👼☁👼"
        self.bottom_border = "☁👼☁👼☁👼☁👼☁👼☁👼"
        self.tileset = HEAVEN_TILES

class Undersea(Scene):
    def __init__(self):
        super(Undersea, self).__init__("undersea")
        self.top_border = "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊"
        self.bottom_border = "🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊🌊"
        self.tileset = UNDERSEA_TILES
        
def maketrain():
    standard_scenes = [Desert, Beach, Forest, Field, Wildflowers]
    special_scenes = [Space, Undersea, Heaven, Hell]

    if random.randint(1,12) == 12:
        scene = random.choice(special_scenes)()
    else:
        scene = random.choice(standard_scenes)()

    return scene.generate()

if __name__ == "__main__":
    maketrain()
