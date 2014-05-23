#!/usr/bin/env python

from dataEmulator import Ticker
from pprint import pprint
import json
from random import randint
from string import ascii_lowercase

json_data = open("data/data.json", 'r')

data = json.load(json_data)
json_data.close()

pprint(data)


# getting the numeric value for each ascii lovercase letter
ascii_letters = [ord(x) for x in ascii_lowercase]
start = ascii_letters[0]
end = ascii_letters[-1]

json_array = []

for x in range(80):
    int_msg = randint(start, end)
    hex_msg = hex(int_msg)
    delay = randint(0, 2)
    tmp_data = {
        "msg": hex_msg,
        "delay": delay,
        "description": ""
    }
    json_array.append(tmp_data)


with open('data/data.json', 'w') as outfile:
    final_array = {
        "data": json_array
    }
    json.dump(final_array, outfile)
