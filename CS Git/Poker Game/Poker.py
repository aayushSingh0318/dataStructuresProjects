#  File: Poker.py

#  Description: Program simulates a 5-Card Draw (Poker) game.


import random
from re import L
import sys

class Card (object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C' , 'D', 'H', 'S')

    #constructor
    def __init__ (self, rank = 12, suit = 'S'):
        if (rank in Card.RANKS):
            self.rank = rank
        else:       #if it doesnt match we give default 
            self.rank = 12

        if (suit in Card.SUITS):
            self.suit = suit
        else:
            self.suit = 'S'

    # string representation of a Card object
    def __str__ (self):
        if (self.rank == 14):
            rank = 'A'
        elif (self.rank == 13):
            rank = 'K'
        elif (self.rank == 12):
            rank = 'Q'
        elif (self.rank == 11):
            rank = 'J'
        else:
            rank = str (self.rank)
        return rank + self.suit

    #equality tests
    def __eq__ (self, other):           #if the cards are equal 
        return self.rank == other.rank

    def __ne__ (self, other):           #if the cards are not equal 
        return self.rank != other.rank

    def __lt__ (self, other):
        return self.rank < other.rank

    def __le__ (self, other):
        return self.rank <= other.rank

    def __gt__ (self, other):
        return self.rank > other.rank

    def __ge__ (self, other):
        return self.rank >= other.rank

class Deck (object):
    #constructor
    def __init__ (self, num_decks = 1):
        self.deck = []
        for i in range (num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append (card)

    #shuffle the deck
    def shuffle (self):
        random.shuffle (self.deck)

    #deal a card
    def deal (self):
        if (len(self.deck) == 0):
            return None
        else:
            return self.deck.pop(0)     #returns the first card in the deck

class Poker (object):
    # constructor
    def __init__ (self, num_players = 2, num_cards = 5): #min num of ppl is 2, and 5 cards
        self.deck = Deck()
        self.deck.shuffle()
        self.players_hands = []         #list of all hands of players
        self.numCards_in_Hand = num_cards

        #deal all the hands
        for i in range(num_players):
            hand = []
            for j in range (self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.players_hands.append (hand)

    #simulate the play of Poker
    def play(self):
        # sort the hands of each player and print the hands
        for i in range (len(self.players_hands)):
            sorted_hand = sorted (self.players_hands[i], reverse = True)
            self.players_hands[i] = sorted_hand                                                        
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print ('Player ' + str(i + 1) + ' : ' + hand_str)


        hand_type = [] #a list to store each combination of hand 
        hand_points = [] #a list to store points for each combo 

        for i in range (len(self.players_hands)):
            sorted_hand = self.players_hands[i]
                #royal flush
            if self.is_royal(sorted_hand)[0]:
                points, type = self.is_royal(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue
                #straight flush
            elif self.is_straight_flush(sorted_hand)[0]:
                points, type = self.is_straight_flush(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue
                #four kind
            elif self.is_four_kind(sorted_hand)[0]:
                points, type = self.is_four_kind(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue
                #full house 
            elif self.is_full_house(sorted_hand)[0]:
                points, type = self.is_full_house(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue
                #flush
            elif self.is_flush(sorted_hand)[0]:
                points, type = self.is_flush(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue
                #staright
            elif self.is_straight(sorted_hand)[0]:
                points, type = self.is_straight(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue
                #three kind
            elif self.is_three_kind(sorted_hand)[0]:
                points, type = self.is_three_kind(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue
                #two pair
            elif self.is_two_pair(sorted_hand)[0]:
                points, type = self.is_two_pair(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue
                #one pair
            elif self.is_one_pair(sorted_hand)[0]:
                points, type = self.is_one_pair(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue
                #highcard
            elif self.is_high_card(sorted_hand)[0]:
                points, type = self.is_high_card(sorted_hand)
                hand_points.append(points)
                hand_type.append(type)
                continue

        #print hand types
        print('')
        for i in range (len(self.players_hands)):
            print('Player ' + str(i + 1) + ': ' + str(hand_type[i]))  #potential issue with [1]
        print('')
        #assign point values to each type so we can compare 
        for i in range(len(hand_type)):
            if hand_type[i] == 'High Card':
                hand_type[i] = 0
            elif hand_type[i] == 'One Pair':
                hand_type[i] = 1
            elif hand_type[i] == 'Two Pair':
                hand_type[i] = 2
            elif hand_type[i] == 'Three of a Kind':
                hand_type[i] = 3
            elif hand_type[i] == 'Straight':
                hand_type[i] = 4
            elif hand_type[i] == 'Flush':
                hand_type[i] = 5
            elif hand_type[i] == 'Full House':
                hand_type[i] = 6
            elif hand_type[i] == 'Four of a Kind':
                hand_type[i] = 7
            elif hand_type[i] == 'Straight Flush':
                hand_type[i] = 8
            elif hand_type[i] == 'Royal Flush':
                hand_type[i] = 9
        #now hand type list is changed values 
        maxval = max(hand_type)
        count = 0 
        for val in hand_type:
            if maxval == val:
                count += 1
        #tie 
        if count > 1:
            ties = []
            for i in range(len(hand_type)):
                if hand_type[i] == maxval:
                    ties.append((hand_points[i], i))
            ties = sorted(ties, reverse = True)
            for k in range(len(ties)):
                print('Player ' + str(ties[k][1] + 1) + ' ties.')
        #winner
        else:
            winner = hand_type.index(maxval)
            print('Player ' + str(winner + 1) + ' wins.')
        '''
        #create dict to find winner/ties
        type_point = {}
        for i in range(len(hand_type)):
            type_point[str(i + 1)] = str(hand_points[i])
        #type_point = dict(zip(hand_type, hand_points))
        #still in def play if u were wondering 
        #find winner 
        winner_pt = 0 
        ties = []
        winnername = ''
        for i in range(1, len(type_point)):
            plyr = str(i)
            plyr_pts = int(type_point[plyr]) #find current player pt 
            if plyr_pts >= winner_pt:
                #to compare each plyr pt to the current winner pt 
                for player in range(i, len(type_point)):
                    #compare for tie between plyr pt and next person in line 
                    if plyr_pts == int(type_point[str(player + 1)]):
                        ties.append(str(player))
                    else:
                        winner_pt = plyr_pts
                        winnername = plyr

                #if plyr pt is greater and not tie, assign new winner 
        #if tie list populated print ties instead of winner 
        if len(ties) > 0:
            for i in range(0, len(ties)):
                tie = ties[i]
                print('Player ' + str(tie) + ' ties.')
        #print winner otherwise
        else:
            print('Player ' + winnername + ' wins.') #player is var we called earlier   ###POTENTAILLY NEEDS A \n
'''
#AAYUSH WORK START HERE
    #find hand combos 
    #royal flush first 
    def is_royal(self, hand):
        #same suit
        royalsuit = True
        for i in range(len(hand) - 1):
            if hand[i].suit != hand[i + 1].suit:
                royalsuit = False
        
        if royalsuit == False:
            return 0, ''
        
        #ranks 
        royalrank = True
        for i in range(len(hand)):
            if hand[i].rank != 14 - i:
                royalrank = False
        
        if royalrank == False:
            return 0, ''

        #points 
        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'
    
    #straight flush 
    def is_straight_flush(self, hand): 
        for i in range(len(hand) - 1):
            #same suit 
            if hand[i].suit == hand[0].suit:
                continue 
            else:
                return 0,''
            
            #consecutive 
        sfcount = 0
        straight_flush = False
        for i in range(len(hand) - 1):
            if hand[i + 1].rank == hand[i].rank - 1:
                sfcount += 1 
        
        if sfcount == 4:
            straight_flush = True
        if straight_flush == False:
            return 0,''

        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush'

    #four kind 
    def is_four_kind(self, hand): 
        #four cards have same rank we dont care about suit 
        #if 4 of the 5 cards have the same rank 
        fourkind = False 
        for i in range(0, len(hand) - 3):
            if hand[i].rank == hand[i + 1].rank == hand[i + 2].rank == hand[i + 3].rank:
                hand.insert(0, hand.pop(i))
                hand.insert(1, hand.pop(i+1))
                hand.insert(2, hand.pop(i+2))
                hand.insert(3, hand.pop(i+3))
                fourkind = True 

        if fourkind == False:
            return 0, ''

        points = 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Four of a Kind'

    #full house 
    def is_full_house(self, hand): 
        fullhouse = False
        if (hand[0].rank == hand[1].rank == hand[2].rank and hand[3].rank == hand[4].rank and hand[2].rank != hand[3].rank) or (hand[0].rank == hand[1].rank and hand[2].rank == hand[3].rank == hand[4].rank and hand[1].rank != hand[2].rank):
            fullhouse = True
        
        if fullhouse != True:
            return 0, ''

        points = 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Full House'

    #flush
    #5 suits 
    def is_flush(self, hand): 
        flush = True
        for i in range(len(hand) - 1):
            if hand[i].suit != hand[0].suit:
                flush = False
                break

        if flush == False:
            return 0,''

        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Flush'

    #straight 
    #consecutive nums only 
    def is_straight(self, hand): 
        #same method as previous funcs 
        straight = False 
        scount = 0 
        for i in range(len(hand) - 1):
            if hand[i + 1].rank == hand[i].rank - 1:
                scount += 1 
        if scount == 4:
            straight = True
        
        if straight == False:
            return 0, ''

        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight'

    #three kind 
    #need to either save places of cards three kind, or move to one place 
    def is_three_kind(self, hand): 
        threekind = False
        for i in range(len(hand) - 2):
            #if three in a row (SORTED) are the same 
            if hand[i].rank == hand[i+1].rank == hand[i + 2].rank:
                #put all three at beginning of hand so that we can calc points 
                hand.insert(0, hand.pop(i))
                hand.insert(1, hand.pop(i + 1))
                hand.insert(2, hand.pop(i + 2))
                threekind = True
        
        if threekind == False:
            return 0, ''
        
        points = 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Three of a Kind'

    #twopair 
    #same concept as three but needs a counter 
    def is_two_pair(self, hand): 
        hand.reverse()
        tpcount = 0
        twopair = False 
        for i in range(len(hand) - 1):
            if hand[i].rank == hand[i + 1].rank:
                tpcount += 1 
                hand.insert(0, hand.pop(i))
                hand.insert(1, hand.pop(i + 1))
        
        if tpcount == 2:
            twopair = True 
        
        if twopair == False:
            return 0, ''
        
        points = 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Two Pair'

    #one pair 
    #no counter otherwise same as previous func 
    def is_one_pair(self, hand): 
        onepair = False 
        for i in range(len(hand) - 1):
            if hand[i].rank == hand[i + 1].rank:
                hand.insert(0, hand.pop(i))
                hand.insert(1, hand.pop(i + 1))
                onepair = True 

        if onepair == False:
            return 0, ''

        points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'One Pair'

    #high card
    #just find points 
    def is_high_card(self, hand): 
        points = 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'High Card'

#AAYUSH WORK END HERE
#IF THE CODE DOES NOT OUTPUT CORRECTLY, I HAVE MADE COMMENTS THROUGHOUT FOR POTENTIAL CHANGES 


def main():
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int (line)
    if ((num_players < 2) or (num_players > 6)):
        return
    
    #create the Poker object 
    game = Poker (num_players)

    #play the game 
    game.play()

#whatever this means 
if __name__ == "__main__":
    main()
        
