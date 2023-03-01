import CoinClass as c

def shown_coin_status(coin_obj):
    print(f"This side is up: {coin_obj.get_sideup()}")

def flip(coing_obj):
    coing_obj.toss()


my_coin = c.Coin()

shown_coin_status(my_coin)
flip(my_coin)
shown_coin_status(my_coin)
