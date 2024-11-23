#!/usr/bin/env python3

import yaml, os
import choochoogen
import time
import random
from mastodon import Mastodon
from twython import Twython


start_delay = random.randint(0,3600)
time.sleep(start_delay)

fullpath = os.path.dirname(os.path.realpath(__file__))

config = yaml.safe_load(open(fullpath + "/config.yaml"))

mc = Mastodon(access_token=config['mastodon_token'],
              api_base_url=config['mastodon_url'])

mc.toot(tweet)
