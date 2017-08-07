#!/usr/bin/env python3

import yaml, os
import choochoogen
import time
import random
from twython import Twython

start_delay = random.randint(0,3600)
time.sleep(start_delay)

fullpath = os.path.dirname(os.path.realpath(__file__))

config = yaml.load(open(fullpath + "/config.yaml"))

twitter_app_key = config['twitter_app_key']
twitter_app_secret = config['twitter_app_secret']
twitter_oauth_token = config['twitter_oauth_token']
twitter_oauth_token_secret = config['twitter_oauth_token_secret']

twitter = Twython(twitter_app_key, twitter_app_secret, twitter_oauth_token, twitter_oauth_token_secret)

tweet = choochoogen.maketrain()

twitter.update_status(status=tweet)
