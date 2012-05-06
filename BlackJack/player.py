#!/usr/bin/python2.6
"""
Black Jack - Player Model
"""
from card import Card

class Player(object):
    
    def __init__(self, balance):
        self._balance = balance
        self.reset()
        
    def reset(self):
        self._card_sets_on_slots = [None] * 4    
        self._bets_on_slots = [0] * 4
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def card_sets_on_slots(self):
        return self._card_sets_on_slots
    
    @card_sets_on_slots.setter
    def card_sets_on_slots(self, value):
        self._card_sets_on_slots = value
        
    @property
    def bets_on_slots(self):
        return self._bets_on_slots
    
    @bets_on_slots.setter
    def bets_on_slots(self, value):
        self._bets_on_slots = value
        