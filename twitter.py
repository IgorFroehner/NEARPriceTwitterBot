from decouple import config
import tweepy

class Twitter:
    def __init__(self):
        self.API_KEY = config('TWITTER_API_KEY')
        self.SECRET_API_KEY = config('TWITTER_SECRET_API_KEY')

        self.ACCESS_TOKEN = config('TWITTER_ACCESS_TOKEN')
        self.SECRET_ACCESS_TOKEN = config('TWITTER_SECRET_ACCESS_TOKEN')

        auth = tweepy.OAuthHandler(self.API_KEY, self.SECRET_API_KEY)
        auth.set_access_token(self.ACCESS_TOKEN, self.SECRET_ACCESS_TOKEN)

        self.api = tweepy.API(auth)

    def send_tweet(self, tweet_text: str):
        try:
            self.api.update_status(tweet_text)
        except tweepy.TweepError as e:
            print('Error while tweeting: ' + e.reason)
