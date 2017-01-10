#!/usr/bin/env python3
from librip.gens import field, gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Кресло', 'price': 1500, 'color': 'brown'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': None, 'price': 100, 'color': 'blue'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1

print(list(field(goods, 'title')))
print(list(field(goods, 'title', 'price')))

print(list(gen_random(1,3,5)))

