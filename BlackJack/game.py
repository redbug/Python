#!/usr/bin/python2.6
"""
Black Jack - Game Model
"""
import sys

from settings import *
from utils import *
from dealer import Dealer

class Game(object):
    PHASE_INITIAL_BETTING  = 0
    PHASE_INITIAL_DEAL     = 1
    PHASE_POST_DEAL        = 2
    PHASE_DEALER           = 3
    PHASE_BET_COLLECTION   = 4
    
    PHASE = [(PHASE_INITIAL_BETTING, "Initial Betting Phase"),
             (PHASE_INITIAL_DEAL, "Initial Deal Phase"),
             (PHASE_POST_DEAL, "Post Deal Action Phase"),
             (PHASE_DEALER, "Dealer Phase"),
             (PHASE_BET_COLLECTION, "Bet Collection Phase"),
             ]
    
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
        
        # Test soft hand
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
    
    def __init__(self, dealer, player):
        self._dealer = dealer
        self._player = player
        self.reset()
        
    def reset(self):
        self._player.reset()
        self._dealer.reset()
        self._phase = Game.PHASE_INITIAL_BETTING
        
    def init_betting_phase(self):
        self._dealer.reset_decks()
        
        print_phase(Game.PHASE[0])
        self.display_player_balance()
        
        while True:
            num_slot = raw_input( message("Select a slot to bet ( [1-4]:slot, s:start game, q:quit game):") )
            
            if num_slot == 'q':
                print_action('Quit Game.')
                sys.exit()
                
            if num_slot == 's':
                print_action('Start Game.')
                
                if reduce(lambda x,y: x+y, self._player.bets_on_slots) != 0: 
                    self._phase = Game.PHASE_INITIAL_DEAL
                    return
                else:
                    print_error("You havn't bet on any slot.")
                    continue
            
            is_valid, num_slot = check_int(num_slot)
            
            if not is_valid:
                print_error("Invalid input.")
            
            elif not Game.check_num_slot(num_slot):
                print_error("Slot number has to be in range [1-4].")
                
            else:
                print_action("Bet on Slot %s." % num_slot)
                while True:
                    bet = raw_input(message("How much to bet? ([%s-%s]:bet, a:abort, w:withdraw):" % (HOUSE_MIN, HOUSE_MAX)) )                    
                    withdraw = False
                    
                    if bet == 'a':
                        print_action("Abort.")
                        break
                    
                    if bet == 'w':
                        print_action("Withdraw.")
                        bet = raw_input(message("Your bet on Slot %s: %s\nHow much will you withdraw from the slot? " % (num_slot, self._player.bets_on_slots[num_slot-1])) )
                        withdraw = True
                    
                    is_valid, bet = check_int(bet)
                    
                    if not is_valid or bet <= 0:
                        print_error("Bet has to be a positive integer.")
                    
                    elif withdraw == False and not self.check_player_balance( bet ):
                        pass
        
                    else:
                        if withdraw:
                            print_action("Withdraw %s." % bet)
                        else:
                            print_action("Bet %s." % bet)
                        print_highlight("Bets on each slot:" +  str(self.bet(num_slot-1, bet, undo=withdraw)) )
                        self.display_player_balance()
                        break                
    
    def init_deal_phase(self):
        print_phase(Game.PHASE[1])
        self.deal()
        print_highlight("Dealer's cards: %s" % self.show_dealer_card(show_first_card=False))
        
        self._phase = Game.PHASE_POST_DEAL
         
    def post_deal_phase(self):
        print_phase(Game.PHASE[2])
        
        for i, card_sets in enumerate( self._player.card_sets_on_slots ):
            if card_sets:
                split_status = False
                print_highlight("Your cards on Slot %d: " % (i+1))
                
                for k, card_set in enumerate(card_sets):

                    while True:
                        points = Game.count_points(card_set)
 
                        print_highlight("card set %s: %s (points: %s)" % ((k+1), card_set, points) )
                        
                        if points == 21:
                            if len(card_set) == 2:
                                print_highlight("Blackjack!")
                            break
                        
                        if points > 21:
                            print_highlight("Bust!")
                            break

                        available_actions = ['h:hit', 's:stand']
                        allow_split = False
                        allow_double = False
                        
                        num_card = len(card_set)
                        if num_card == 2:
                            if card_set[0].pip == card_set[1].pip:
                                allow_split = True
                            allow_double = True
                        
                        if allow_split:
                            available_actions.append('t:split')
                        if allow_double and not split_status:
                            available_actions.append('d:doouble down')
                        act = raw_input("(" + ', '.join(available_actions) +"): ")
                        
                        if act == "h":
                            print_action("Hit.")
                            card_set.extend( self._dealer.draw_cards_from_deck(1) )
                        elif act == "s":
                            print_action("Stand.")
                            break
                        elif act == "t" and allow_split == True:
                            print_action("Split.")
                            split_status = True
                            
                            original_bet = self._player.bets_on_slots[i]
                            if self.check_player_balance(original_bet):
                                self._player.balance -= original_bet
                                print_highlight("Place a second bet for the new splited card set: %s" % original_bet)
                                self.display_player_balance() 
                                print_highlight("%s ->" % card_set)
                                
                                # split the original card set to two new card sets.
                                new_card_set = [card_set.pop()]
                                
                                card_set.extend(self._dealer.draw_cards_from_deck(1))
                                new_card_set.extend(self._dealer.draw_cards_from_deck(1))
                                card_sets.append(new_card_set)
                                
                                print_highlight(card_set)
                                print_highlight(new_card_set)
                            
                        elif act == "d" and allow_double and not split_status:
                            print_action("Double down on slot %s." % (i+1))
                            original_bet = self._player.bets_on_slots[i]
                            
                            # When you double down, you must take one additional card and 
                            # you cannot receive more than one.
                            if self.check_player_balance(original_bet):
                                print_highlight( "Bets on each slot:" +  str(self.bet(i, original_bet, double=True)) )
                                self.display_player_balance()
                                
                                print_highlight("Take one additional card.")
                                card_set.extend( self._dealer.draw_cards_from_deck(1) )
                                
                                points = Game.count_points(card_set)
                                print_highlight("card set %s: %s (points: %s)" % ((k+1), card_set, points) )
                                break
                        else:
                            print_error("Invalid input.")
            
        self._phase = Game.PHASE_DEALER 
    
    def dealer_phase(self):
        print_phase(Game.PHASE[3])
        
        while True:
            dealer_points = Game.count_points(self._dealer.cards)
            print_highlight( "Dealer's cards: %s (points: %s)" % (self.show_dealer_card(show_first_card=True), Game.count_points(self._dealer.cards)) )
            
            if dealer_points <= 16:
                self._dealer.cards.extend( self._dealer.draw_cards_from_deck(1) )
            elif dealer_points > 21:
                print_highlight("Dealer Bust!")
                break
            else:
                if dealer_points == 21:
                    print_highlight("Dealer Blackjack!")
                break
                
        self._phase = Game.PHASE_BET_COLLECTION
    
    def bet_collection_phase(self):
        print_phase(Game.PHASE[4])
        
        for i, card_sets in enumerate( self._player.card_sets_on_slots ):
            if card_sets:
                bet = self._player.bets_on_slots[i]
                
                print_highlight( "Your cards on Slot %d: " % (i+1) )
                for k, card_set in enumerate(card_sets):                    
                    points = Game.count_points(card_set) 
                    msg =  "Card set %s: %s (points: %s)" % ((k+1), card_set, points)

                    result, award = self.judge(card_set, bet)
            
                    if result == Dealer.WIN:
                        print_highlight( msg + " -> You lose %s bet." % bet ) 
                        
                    if result == Dealer.LOSE:
                        self._player.balance += bet + award
                        print_highlight( msg + " -> You win %s bet." % award ) 
                        
                    if result == Dealer.TIE:
                        self._player.balance += bet
                        print_highlight( msg + " -> Game Tie." )

        self.reset()
    
    def judge(self, card_set, bet):
        total_points = Game.count_points(card_set)
        dealer_total_points = Game.count_points(self._dealer.cards)
        
        dealer_total_points = 0 if dealer_total_points > 21 else dealer_total_points
        total_points = 0 if total_points > 21 else total_points
        
        if total_points == 0:
            return Dealer.WIN, 0
        
        if dealer_total_points > total_points:
            return Dealer.WIN, 0
        elif dealer_total_points < total_points:
            # Player wins two bets because of Blackjack.
            if total_points == 21 and len(card_set) == 2:
                return Dealer.LOSE, bet * 2
            return Dealer.LOSE, bet
        else:
            return Dealer.TIE, 0
    
    def display_player_balance(self):
        print_highlight("Your balance: %s" % self._player.balance)
        
    def show_dealer_card(self, show_first_card=False):
        if show_first_card:
            return self._dealer.cards
        else:
            return "[ " + "*Hole Card*, " + ", ".join( [str(card) for i, card in enumerate(self._dealer.cards) if i > 0]) + " ]"
            
    def check_player_balance(self, bet):
        if bet > self._player.balance:
            print_error("Your balance is not enough.")
            return False
        return True
    
    def bet(self, num_slot, bet, undo=False, double=False):
        bet_on_slot = self._player.bets_on_slots[num_slot]
        
        # withdraw bet from a slot
        if undo == True:
            if bet_on_slot >= bet:
                self._player.balance += bet
                self._player.bets_on_slots[num_slot] -= bet
            else:
                print_error( "Your bet on slot %s is %s. You can't withdraw %s bet from it." % (num_slot+1, bet_on_slot, bet) )   
        # bet on a slot
        else:
            after_bet_on_slot = bet_on_slot + bet 
            
            if not double and (after_bet_on_slot < HOUSE_MIN or after_bet_on_slot > HOUSE_MAX):
                print_error("The bet on the slot must within [%s, %s]" % (HOUSE_MIN, HOUSE_MAX))
            else:
                self._player.balance -= bet
                self._player.bets_on_slots[num_slot] += bet                     

        return self._player.bets_on_slots

    def deal(self):
        self._dealer.cards = self._dealer.draw_cards_from_deck(2)
        
        for i, bet in enumerate(self._player.bets_on_slots):
            if bet != 0:
                self._player.card_sets_on_slots[i] = [self._dealer.draw_cards_from_deck(2)]
        
        return (self._dealer.cards, self._player.card_sets_on_slots)
        
    def run(self):
        {
         Game.PHASE_INITIAL_BETTING: self.init_betting_phase,
         Game.PHASE_INITIAL_DEAL: self.init_deal_phase,
         Game.PHASE_POST_DEAL: self.post_deal_phase,
         Game.PHASE_DEALER: self.dealer_phase,
         Game.PHASE_BET_COLLECTION: self.bet_collection_phase
         }[self._phase]()
         
        return True
    