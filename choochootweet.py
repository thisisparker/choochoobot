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

twitter_app_key = config['twitter_app_key']
twitter_app_secret = config['twitter_app_secret']
twitter_oauth_token = config['twitter_oauth_token']
twitter_oauth_token_secret = config['twitter_oauth_token_secret']

twitter = Twython(twitter_app_key, twitter_app_secret, twitter_oauth_token, twitter_oauth_token_secret)

mc = Mastodon(access_token=config['mastodon_token'],
              api_base_url=config['mastodon_url'])

tweet = choochoogen.maketrain()

mc.toot(tweet)
twitter.update_status(status=tweet)
