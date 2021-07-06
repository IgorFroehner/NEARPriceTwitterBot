
import tweepy
from decouple import config

if __name__ == '__main__':
    API_KEY = config('TWITTER_API_KEY')
    SECRET_API_KEY = config('TWITTER_SECRET_API_KEY')

    auth = tweepy.OAuthHandler(API_KEY, SECRET_API_KEY)

    redirect_url = auth.get_authorization_url()
    print(f"Enter in this url: {redirect_url}")

    verifier = input('Input the verifier token here: ')

    token = None
    try:
        token = auth.get_access_token(verifier)
    except tweepy.TweepError:
        print('Error! Failed to get access token.')

    print(f'TWITTER_ACCESS_TOKEN: {token[0]}')
    print(f'TWITTER_SECRET_ACCESS_TOKEN: {token[1]}')
