#!/usr/bin/python2.6
from settings import *

class Card(object):
    
    def __init__(self, id):
        assert id >= 0 and id < NUM_CARDS
        
        self._id = id
        self._pip = id / NUM_PIP
        self._suit = id % NUM_SUIT
        
    @property
    def id(self):
        return self._id
    
    @property
    def pip(self):
        return self._pip
    
    @property
    def suit(self):
        return self._suit

    def __repr__(self):
        return "%s %s" % (SUIT_NAME[self._suit], self._pip + 1)
    
    