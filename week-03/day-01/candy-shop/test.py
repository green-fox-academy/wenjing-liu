from sweet import Sweet
from candie import Candie
from lollipop import Lollipop
from candy_shop import CandyShop

def test():
  candie = Candie()
  candie_2= Candie()
  lollipop = Lollipop()
  candy_shop = CandyShop(200)
  candy_shop.create_sweet(candie)
  candy_shop.create_sweet(candie_2)
  candy_shop.create_sweet(lollipop)
  print(candy_shop.to_string())

  candy_shop.raise_price(2)
  print(candy_shop.to_string())
  candy_shop.sell('candie', 1)
  candy_shop.buy_sugar(20)
  print(candy_shop.to_string())

test()