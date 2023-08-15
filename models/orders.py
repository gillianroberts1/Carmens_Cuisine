from models.order import *
import datetime

chilli_con_carne = 'chilli.jpg'
seafood_paella = 'paella.jpg'
sushi = 'sushi.jpg'

order1 = Order(datetime.date(2023, 8, 10), "Gillian", "Chilli Con Carne", 12.50)
order2 = Order(datetime.date(2023, 8, 12), "Carmen", "Seafood Paella", 13.50)
order3 = Order(datetime.date(2023, 8, 13), "Louise", "Sushi", 15.00)

orders = [order1, order2, order3]
