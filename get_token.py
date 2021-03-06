
import tweepy
from decouple import config

if __name__ == '__main__':
    API_KEY = config('TWITTER_API_KEY')
    SECRET_API_KEY = config('TWITTER_SECRET_API_KEY')

    auth = tweepy.OAuthHandler(API_KEY, SECRET_API_KEY)

    redirect_url = auth.get_authorization_url()
    print(f"Access this url: {redirect_url}")

    verifier = input('Paste the verifier token here: ')

    try:
        token = auth.get_access_token(verifier)

        print(f'TWITTER_ACCESS_TOKEN: {token[0]}')
        print(f'TWITTER_SECRET_ACCESS_TOKEN: {token[1]}')
    except tweepy.TweepError:
        print('Error! Failed to get access token.')
