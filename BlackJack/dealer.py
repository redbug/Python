#!/usr/bin/python2.6

import random

from card import Card, NUM_CARDS
from player import Player
from settings import *

class Dealer(Player):
    WIN = 0
    LOSE = 1
    TIE = 2
    
    def __init__(self, name, balance, player):
        assert isinstance(player, Player)
        super(Dealer, self).__init__(name, balance)
        self._player = player
        self.reset_decks()
        self.shuffle()
        
    def reset_decks(self):
        self._decks = [Card(i) for i in range(NUM_CARDS)] * NUM_DECKS
            
    def shuffle(self):
        random.shuffle(self._decks)            
                     
    def draw_cards_from_deck(self, num_card=1):        
        assert len(self._decks) > num_card
        return [self._decks.pop() for i in range(num_card)] 
    
    def deal_card_to_player(self):
        self._player.add_card( self.draw_from_deck() )
        
    def deal_card_to_dealer(self):
        self.add_card( self.draw_from_deck() )
        
    def init_deal(self):
        self.deal_card_to_player()
        self.deal_card_to_player()
        
        self.deal_card_to_dealer()
        self.deal_card_to_dealer()
    
    def deal_cards_to_dealer_until_stop(self):
        while self.total_points() < 17:
            self.deal_card_to_dealer()
        
        
#    def add_card(self, card):
#        super(Dealer, self).add_card(card)
    
    def judge(self):
        dealer_total_points = self.total_points()
        player_total_points = self._player.total_points()
        
        dealer_total_points = 0 if dealer_total_points > 21 else dealer_total_points
        player_total_points = 0 if player_total_points > 21 else player_total_points
        
        if dealer_total_points > player_total_points:
            return Dealer.WIN
        elif dealer_total_points < player_total_points:
            return Dealer.LOSE
        else:
            return Dealer.TIE
    