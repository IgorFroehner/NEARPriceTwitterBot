
from twitter import Twitter
from near import Near
from time import sleep

if __name__ == '__main__':

    near = Near()
    twitter = Twitter()

    while True:
        data = near.getData()
        price = f'{data["price"]:.2f}'.replace('.', ',')
        percent_change_24h = f'{data["percent_change_24h"]:.2f}'.replace('.', ',')
        twitter.send_tweet(f'1 #NEAR = {price} #BRL agora. ({percent_change_24h} % nas últimas 24hrs)')
        sleep(3600)
