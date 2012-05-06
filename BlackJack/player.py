#!/usr/bin/python2.6
"""
Black Jack - Player Class
"""
from card import Card

class Player(object):
    
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = value

    