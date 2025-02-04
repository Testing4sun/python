# Вложенные классы

from address import Address
from mailing import Mailing

to_address = Address("101010", "Москва", "Пушкина", "10", "45")
from_address = Address("301450", "Санкт-Петербург", "Колотушкина", "5", "112")

mailing = Mailing(to_address, from_address, "1420", "DF55550006")

print(mailing)
