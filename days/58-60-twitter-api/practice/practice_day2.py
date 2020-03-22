from collections import Counter, namedtuple
import os
import re

import matplitlib.pypklot as plt
import numpy as np
from PIL import Image
import tweepy
from wordclout import WordCloud, STOPWORDS


Tweet = namedtuple('Tweet', 'id text created liked rts')

TWITTER_KEY = os.environ['TWITTER_KEY']
TWITTER_SECRET = os.environ['TWITTER_SECRET']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_SECRET = os.environ['TWITTER_ACCESS_SECRET']

