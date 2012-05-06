#!/usr/bin/python2.6
"""
Black Jack - Dealer Model
"""
import random

from card import Card, NUM_CARDS
from player import Player
from settings import *

class Dealer(Player):
    WIN = 0
    LOSE = 1
    TIE = 2
    
    def __init__(self, num_decks=NUM_DECKS ):
        self._num_decks = num_decks
        self.reset()
        
    def reset(self):
        self._cards = []
    
    @property
    def cards(self):
        return self._cards
    
    @cards.setter
    def cards(self, value):
        self._cards = value
        
    def reset_decks(self):
        self._decks = [Card(i) for i in range(NUM_CARDS)] * self._num_decks
        self.shuffle()
        
        #for testing card split
        #self._decks.extend([Card(1)] * 5)        
            
    def shuffle(self):
        random.shuffle(self._decks)            
                     
    def draw_cards_from_deck(self, num_card=1):        
        assert len(self._decks) > num_card
        return [self._decks.pop() for i in range(num_card)] 