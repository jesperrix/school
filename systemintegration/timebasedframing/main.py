#!/usr/bin/env python

from dataEmulator import Ticker
from pprint import pprint
import json

ticker = Ticker(500)

json_data = open("data/data.json", 'r')

data = json.load(json_data)
json_data.close()

#delay
tickDelay = 0

#timeout
tickTimeout = 0

#bytes container
containedBytes = []

while(True):
    """
    Main loop to emulate data stream
    """
    #  check if timeout is reached and there is bytes in the container
    if tickTimeout == 0 and len(containedBytes) > 0:
        pprint(containedBytes)
        containedBytes == []

    # check if tick delay isset else read data and put it into containedBytes
    tickTimeout -= 1
    if tickDelay > 0:
        tickDelay -= 1
    else:
        try:
            byte = data["data"].pop(0)
            msg = byte["msg"]
            tickDelay = byte["delay"]
            containedBytes.append(msg)
            # set tickTimeout each time a
            tickTimeout = 4
        except Exception:
            print "No more values to read"
            break

    ticker.tick()
