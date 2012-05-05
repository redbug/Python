#!/usr/bin/python2.6

import sys

from settings import *
from utils import check_float, check_int
from dealer import Dealer

class Game(object):
    #TODO: split, double down, 5 more cards
    
    PHASE_INITIAL_BETTING  = 0
    PHASE_INITIAL_DEAL     = 1
    PHASE_POST_DEAL        = 2
    PHASE_DEALER           = 3
    PHASE_BET_COLLECTION   = 4
    
    def __init__(self, dealer, player):
        self._dealer = dealer
        self._player = player
        self.reset()
        
    def reset(self):
        self._bets_on_slots = [0] * 4
        self._cards_on_slots = [None] * 4
        self._double_down_on_slots = [False] * 4
        self._dealer_cards = []
        self._phase = Game.PHASE_INITIAL_BETTING
        
    def init_betting_phase(self):
        
        print " == Initial Betting Phase == "
        print "Your balance: %s" % self._player.balance
        
        while True:
            num_slot = raw_input("Select a slot to bet (slot:[1-4], n:done):")
            
            if num_slot == 'n':
                self._phase = Game.PHASE_INITIAL_DEAL
                return
            
            is_valid, num_slot = check_int(num_slot)
            
            if not is_valid:
                print "Invalid input: You should give me a integer (1-4)."
            
            elif not Game.check_num_slot(num_slot):
                print "slot number must in range [1, 4]"
            else:
                break
        
        while True:
            bet = raw_input("How much to bet on Slot %s (bet: [%s-%s], 0:revoke, w:withdraw):" % (num_slot, HOUSE_MIN, HOUSE_MAX) )
            
            withdraw = False
            if bet == 'w':
                bet = raw_input("Your bet on Slot %s: %s\nHow much will you withdraw from it? " % (num_slot, self._bets_on_slots[num_slot-1]) )
                withdraw = True
            
            is_valid, bet = check_float(bet)
            
            if not is_valid:
                print "Invalid input: You should give me a number."
            elif bet < 0:
                print "Invalid input: You should give me a positive number."
            elif bet == 0:
                print "You revoke to bet on slot %s." % num_slot
            
            elif withdraw == False and bet > self._player.balance:
                print "Your balance is not enough to bet."
                        
            else:
                print self.bet(num_slot, bet, undo=withdraw)
                print "Your balance: %s" % self._player.balance
                break                
    
    def init_deal_phase(self):
        
        print "\n == Initial Deal Phase == "
        #TODO: Dealer on hole card
        dealer_cards, player_cards = self.deal()
        print "Dealer's cards: %s (points: %s)" % (dealer_cards, Game.count_points(dealer_cards) )
        
        self._phase = Game.PHASE_POST_DEAL
         
    def post_deal_phase(self):

        print "\n == Post Deal Action Phase == "
        
        for i, card_set in enumerate( self._cards_on_slots ):
            if card_set:
                while True:
                    points = Game.count_points(card_set) 
                    print "Your cards on Slot %s: %s (points: %s)" % (i+1, card_set, points)
                    
                    if points == 21:
                        print "Blackjack!"
                        break
                    
                    if points > 21:
                        print "Bust!"
                        break
                 
                    #TODO: more than 5 cards
                    available_actions = ['h:hit', 's:stand']
                    allow_split = False
                    allow_double = False
                    
                    if len(card_set) == 2:
                        if card_set[1].pip == card_set[2].pip:
                            allow_split = True
                        allow_double = True
                    
                    if allow_aplit:
                        available_actions.append('s:split')
                    if allow_double:
                        available_actions.append('d:doouble')
                    action = raw_input("(" + ', '.join(available_actions) +"): ")
                    
                    if action == "h":
                        card_set = self.hit(i+1)
                    elif action == "s":
                        break
                    else:
                        print "Invalid input."
        
        self._phase = Game.PHASE_DEALER 
    
    def dealer_phase(self):
        print "\n == Dealer Phase == "
        while True:
            dealer_points = Game.count_points(self._dealer_cards)
            print "Dealer's cards: %s (points: %s)" % (self._dealer_cards, Game.count_points(self._dealer_cards) )
            
            if dealer_points <= 16:
                self._dealer_cards.extend( self._dealer.draw_cards_from_deck(1) )
            elif dealer_points > 21:
                print "Dealer Bust!"
            else:
                if dealer_points == 21:
                    print "Dealer Blackjack!"
                elif dealer_points < 21:
                    print "Dealer's final cards: %s (points: %s)" % (self._dealer_cards, Game.count_points(self._dealer_cards) )
                break
                
        self._phase = Game.PHASE_BET_COLLECTION
    
    def bet_collection_phase(self):
        print "\n == Bet Collection Phase == "
        
        print "Dealer's cards: %s (points: %s)" % (self._dealer_cards, Game.count_points(self._dealer_cards) )
        
        for i, card_set in enumerate( self._cards_on_slots ):
            if card_set:
                bet = self._bets_on_slots[i]
                print "Your cards on Slot %s: %s (points: %s)" % (i+1, card_set, Game.count_points(card_set) )
                result, award = self.judge(card_set, bet)
                
                if result == Dealer.WIN:
                    print "You lose %s bet." % bet 
                    
                if result == Dealer.LOSE:
                    self._player.balance += award
                    print "You win %s bet. Balance: %s" % ( award, self._player.balance) 
                    
                if result == Dealer.TIE:
                    print "Game Tie."
            
        self.reset()
    
    def judge(self, card_set, bet):
        total_points = Game.count_points(card_set)
        dealer_total_points = Game.count_points(self._dealer_cards)
        
        dealer_total_points = 0 if dealer_total_points > 21 else dealer_total_points
        total_points = 0 if total_points > 21 else total_points
        
        if dealer_total_points > total_points:
            return Dealer.WIN, 0
        elif dealer_total_points < total_points:
            return Dealer.LOSE, bet * 1
        else:
            return Dealer.TIE, 0

    
    def start(self):        
        self._dealer.init_deal()
        self._dealer.show_cards()
        self._player.show_cards()
    
    @classmethod
    def count_points(cls, card_set):        
        total = 0
        credit = 0
        for card in card_set:
            point = card.pip + 1
            if point == 1:
                credit += 1
            elif point > 10:
                point = 10
            total += point
        
        """ Test soft hand """
        for i in range(credit):
            if total + 10 <= 21:
                total += 10
            else:
                break
            
        return total    
    
    @classmethod
    def check_num_slot(cls, num_slot):
        if int(num_slot) not in range(1,5):
            return False
        return True
        
    def bet(self, num_slot, bet, undo=None):
        """    
        blackjack-bet - takes a slot number (int), bet amount (float). Must check for validity of slot numbers (1-4). 
        Must check if bet is within house minimum and maximum. 
        Must check if bet is not over player balance. 
        Optional parameter, undo (boolean) if set, removes the bet amount from the slot number. 
        Returns total bet amounts for each slot.
        """
        bet_on_slot = self._bets_on_slots[num_slot-1]
        if undo == True:
            if bet_on_slot >= bet:
                self._player.balance += bet
                self._bets_on_slots[num_slot-1] -= bet
            else:
                print "Your bet on slot %s is %s. You can't withdraw %s bet from it." % (num_slot, bet_on_slot, bet)   
        else:
            after_bet_on_slot = bet_on_slot + bet 
            if after_bet_on_slot < HOUSE_MIN or after_bet_on_slot > HOUSE_MAX:
                print "The bet on the slot must within [%s, %s]" % (HOUSE_MIN, HOUSE_MAX) 
            else:               
                self._player.balance -= bet
                self._bets_on_slots[num_slot-1] += bet
        return self._bets_on_slots

    def deal(self):
        """
        blackjack-deal - starts the game. 
        Returns the cards in all slots that have bets on them as well as the dealer's cards.
        """
        self._dealer_cards = self._dealer.draw_cards_from_deck(2)
        
        for i, bet in enumerate(self._bets_on_slots):
            if bet != 0:
                self._cards_on_slots[i] = self._dealer.draw_cards_from_deck(2)
        
        return (self._dealer_cards, self._cards_on_slots)

    def hit(self, num_slot):
        """
        blackjack-hit - takes a slot number (int), 
        returns hand in the slot plus the new card from the hit.
        """
        if not Game.check_num_slot(num_slot):
            print "slot number must in range [1, 4]"
        
        elif self._bets_on_slots[num_slot-1] == 0:
            print "You have no bet on slot %s" % num_slot
        
        else:
            self._cards_on_slots[num_slot-1].extend( self._dealer.draw_cards_from_deck(1) )
        
        return self._cards_on_slots[num_slot-1]
    
    def stand(self, num_slot):
        """
        blackjack-stand - takes a slot number (int), 
        returns the hand in the slot.
        """
        if not Game.check_num_slot(num_slot):
            print "slot number must in range [1, 4]"
        
        elif self._bets_on_slots[num_slot-1] == 0:
            print "You have no bet on slot %s" % num_slot
            
        return self._cards_on_slots[num_slot-1]
        
    def run(self):
        {
         Game.PHASE_INITIAL_BETTING: self.init_betting_phase,
         Game.PHASE_INITIAL_DEAL: self.init_deal_phase,
         Game.PHASE_POST_DEAL: self.post_deal_phase,
         Game.PHASE_DEALER: self.dealer_phase,
         Game.PHASE_BET_COLLECTION: self.bet_collection_phase
         }[self._phase]()
         
        return True
    
    def show(self, dealer, player):
        pass
    
    def more_card(self):
        pass
    
    def enough(self):
        pass
    
    def restart(self):
        pass
    
    def quit():
        pass
    
    