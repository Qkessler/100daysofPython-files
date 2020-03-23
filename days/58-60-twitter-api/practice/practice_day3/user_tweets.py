import tweet_api


class UserTweets:
    
    def __init__(self, twitter_handle):
        self.twitter_handle = twitter_handle
        # self.max_id = max_id
        self.tweets = self.get_tweets()

    def get_tweets(self):
        api = tweet_api.init()
        tweets = []
        for _ in range(5):
            tweets.append(api.user_timeline(self.twitter_handle))
        return tweets
