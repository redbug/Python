#!/usr/bin/python2.6
"""
Blackjack Game Entry
"""

from game import Game
from dealer import Dealer
from player import Player
from utils import check_int
import sys


def main():
    usage_msg = "Usage: python %s player_balance [ number_of_card_decks ]" % __file__
    num_argv = len(sys.argv)
    
    if num_argv not in (2, 3):
        print usage_msg; sys.exit()
    
    else:
        
        is_valid, num = check_int(sys.argv[1])
        if is_valid:
            player_balance = num
        else:
            print "Invalid parameter: %s" % sys.argv[1]
            print usage_msg; sys.exit()
        
        num_decks = None
        if num_argv == 3:
            is_valid, num = check_int(sys.argv[2])
            
            if is_valid:
                num_decks = num
            else:
                print "Invalid parameter: %s" % sys.argv[2]
                print usage_msg; sys.exit()
                
    player = Player(player_balance)
    dealer = Dealer(num_decks) if num_decks else Dealer()
    game = Game(dealer, player)
    
    while game.run():
        pass

if __name__ == "__main__": main()
