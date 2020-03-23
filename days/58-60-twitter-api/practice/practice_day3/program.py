import tweet_api
from user_tweets import UserTweets
from pprint import pprint
import json



if __name__ == '__main__':
    api = tweet_api.init()
    public_tweets = api.home_timeline()
    # pprint(public_tweets[0])
    # me = api.me()
    # print(me)
    user = UserTweets('@quique_kessler')
    tweets = user.get_tweets()
    # json_tweets = json.dumps(tweets._json)
    # statuss = []
    # for status in tweets:
    #     statuss.append()
    print(tweets)
