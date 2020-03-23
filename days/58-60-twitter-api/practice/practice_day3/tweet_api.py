from collections import Counter, namedtuple
import os
import re

import numpy as np
from PIL import Image
import tweepy
from wordcloud import WordCloud, STOPWORDS


Tweet = namedtuple('Tweet', 'id text created liked rts')

TWITTER_KEY = os.environ['TWITTER_KEY']
TWITTER_SECRET = os.environ['TWITTER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']


def init():
    auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
    return tweepy.API(auth)
