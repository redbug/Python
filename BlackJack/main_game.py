#!/usr/bin/python2.6

from game import Game
from dealer import Dealer
from player import Player

def main():
    player = Player("Player", 20)
    dealer = Dealer("Dealer", 20, player)
    game = Game(dealer, player)
    
    while game.run():
        pass

if __name__ == "__main__": main()
