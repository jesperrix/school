#!/usr/bin/env python

from time import sleep


class Ticker():
    """
    Ticker class
    """

    def __init__(self, interval=500):
        """
        takes interval as miliseconds
        """
        self.interval = float(interval) / 1000

    def tick(self):
        """
        do a tick
        """
        sleep(self.interval)
