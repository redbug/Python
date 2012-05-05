#!/usr/bin/python2.6

from card import Card

class Player(object):
    
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self.reset()

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        self._balance = value

    def reset(self):
        self._cards = []
        self._is_show_all = False
    
    def add_card(self, card):
        assert isinstance(card, Card) 
        self._cards.append(card)
    
    def total_points(self):        
        total = 0
        credit = 0
        for card in cards:
            point = card.pip + 1
            if point == 1:
                credit += 1
            elif point > 10:
                point = 10
            total += point
        
        """ Test soft hand """
        for i in range(credit):
            if total + 11 <= 21:
                total += 11
            else:
                break
            
        return total

    def open_first_card(self):
        self._is_show_all = True
    
    def show_cards(self):
        print self._cards
        ", ".join(str(self._cards))
    
    def __repr__(self):
        return "%s - current credits: %s" % (self._name, self._balance)
    