from item import Item
from phone import Phone

# Item.instantiate_from_csv()
# print(Item.pay_rate)
# print(Item.is_integer(7.5))

# phone1 = Phone("Samsung", 500, 5, 1)
# print(phone1.calculate_total_price())
phone2 = Item("iPhone", 700, 5)
# print(Item.all)
phone2.apply_increment(0.2)
print(phone2.price)
phone2.send_email()
phone2.connect()
