from near import Near
from time import sleep
from decouple import config

import tweepy

if __name__ == '__main__':
    API_KEY = config('TWITTER_API_KEY')
    SECRET_API_KEY = config('TWITTER_SECRET_API_KEY')

    ACCESS_TOKEN = config('TWITTER_ACCESS_TOKEN')
    SECRET_ACCESS_TOKEN = config('TWITTER_SECRET_ACCESS_TOKEN')

    auth = tweepy.OAuthHandler(API_KEY, SECRET_API_KEY)
    auth.set_access_token(ACCESS_TOKEN, SECRET_ACCESS_TOKEN)

    api = tweepy.API(auth)

    near = Near()

    while True:
        data = near.getData()
        price = f'{data["price"]:.2f}'.replace('.', ',')
        percent_change_24h = f'{data["percent_change_24h"]:.2f}'.replace('.', ',')
        try:
            api.update_status(f'1 $NEAR = {price} #BRL agora. ({percent_change_24h} % nas últimas 24hrs)')
        except tweepy.TweepError as e:
            print('Error while tweeting: ' + e.reason)
        sleep(43200)
