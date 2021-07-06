from time import sleep
from decouple import config

from near import Near
from twitter import Twitter

if __name__ == '__main__':

    near = Near()
    twitter = Twitter()

    CURRENCY = config('CURRENCY_TO_CONVERT')
    TEXT_LAST_24_HRS = config('TEXT_LAST_24_HRS')

    sleep_time = 86400 / int(config('TWEETS_PER_DAY'))

    while True:
        data = near.getData()
        price = f"{data['price']:.2f}"
        percent_change_24h = f"{data['percent_change_24h']:.2f}"

        twitter.send_tweet(f'1 $NEAR = {price} #{CURRENCY} ({percent_change_24h}% {TEXT_LAST_24_HRS})')

        sleep(sleep_time)
