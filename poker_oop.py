# Constants
suits = 'CDHS'
ranks = '23456789TJQKA'

from abc import ABCMeta, abstractmethod

class Card(metaclass=ABCMeta):
    """Abstact class for playing cards
    """
    def __init__(self, rank_suit):
        if rank_suit[0] not in ranks or rank_suit[1] not in suits:
            raise ValueError(f'{rank_suit}: illegal card')
        self.card = rank_suit
        
    def __repr__(self):
        return self.card
    
    @abstractmethod
    def value(self):
        """Subclasses should implement this method
        """
        raise NotImplementedError("value method not implemented")

    # card comparison operators
    def __gt__(self, other): return self.value() > other.value()
    def __ge__(self, other): return self.value() >= other.value()
    def __lt__(self, other): return self.value() < other.value()
    def __le__(self, other): return self.value() <= other.value()
    def __eq__(self, other): return self.value() == other.value()
    def __ne__(self, other): return self.value() != other.value()

class PKCard(Card):
    """Card for Poker game
    """
    values = dict(zip(ranks, range(2,2+len(ranks))))
    def __init__(self,rank_suit):
        Card.__init__(self,rank_suit)
        self.point=PKCard.values[rank_suit[0]]
        self.suit=rank_suit[1]
        
    def value(self):
        return self.point


if __name__ == '__main__':
    c1 = PKCard('QC')
    c2 = PKCard('9D')
    c3 = PKCard('9C')
    print(f'{c1} {c2} {c3}')
    
    # comparison
    print(c1 > c2==c3)

    # sorting
    cards = [c1, c2, c3, PKCard('AS'), PKCard('2D')]
    sorted_cards = sorted(cards)
    print(sorted_cards)
    cards.sort()
    print(cards)


import random
class Deck:
    def __init__(self, cls):
        """Create a deck of 'cls' card class
        """
        self.cards = [cls(r + s) for s in suits for r in ranks]
        self.rand = random.Random(113)
    def shuffle(self):
        self.rand.shuffle(self.cards)
    
    def pop(self):
        if not self.cards:
            raise ValueError("No more cards")
        return self.cards.pop()
    def __repr__(self):
        return "{}".format(repr(self.cards))
    def __getitem__(self, index):
        return self.cards[index]
    def __len__(self):
        return len(self.cards)

if __name__ == '__main__':
    deck = Deck(PKCard)  # deck of poker cards
    deck.shuffle()
    c = deck[0]
    print('A deck of', c.__class__.__name__)
    print(deck)
    # testing __getitem__ method
    print(deck[-5:])

    while len(deck) >= 10:
        my_hand = []
        your_hand = []
        for i in range(5):
            for hand in (my_hand, your_hand):
                card = deck.pop()
                hand.append(card)
        my_hand.sort(reverse=True)
        your_hand.sort(reverse=True)
        print(my_hand, '>', your_hand, '?', my_hand > your_hand)
  
import random
from collections import defaultdict



class Hands:
   
    def __init__(self, cards):
        if len(cards) != 5:
            raise ValueError('not 5 cards')
        self.cards = sorted(cards, reverse=True)
        
    def is_flush(self):
        f= []
        for i in range(5):
            f.append(self.cards[i][1])
        if f.count(self.cards[0][1]) == 5:    
            return True
        else:    
            return False
        
    def is_straight(self):
        for i in range(4):
            if (values[self.cards[i][0]] - values[self.cards[i+1][0]] == 1):
                return True
            
            else:
                return False   
            
    def classify_by_rank(self):
        list_dict = defaultdict(list)
        for i, j in self.cards:
            list_dict[i].append(j)
    
        return list_dict  
    
    def find_a_kind(self):
        cards_by_ranks = self.classify_by_rank()
        checkPair = list(cards_by_ranks.values())
    
        paircount = []
        for i in range(len(checkPair)):
            paircount.append(len(checkPair[i]))
        if paircount.count(2) == 1 and paircount.count(3) == 1:
            return '<Full house>'
        elif paircount.count(2) == 1:
            return '<One pair>'           
        elif paircount.count(2) == 2:
            return '<Two pair>'
        elif paircount.count(3) == 1:
            return '<Three of a kind>'
        elif paircount.count(4) == 1:
            return '<Four of a kind>'
        elif paircount.count(1) == 5:
            return '<High card>'
        else:
            return None   
        
    def tell_hand_ranking(self):
        if self.is_flush():
            if self.is_straight():
                return '<Straight flush>'
            else:
                return '<Flush>'

        elif self.is_straight():
            return '<Straight>'

        elif self.find_a_kind():
            return self.find_a_kind()
        else:
            return None    
        
    def ranking_menu(self):
        if self.tell_hand_ranking() == '<Straight flush>':
            return 9
        elif self.tell_hand_ranking() == '<Four of a kind>':
            return 8
        elif self.tell_hand_ranking() == '<Full house>':
            return 7
        elif self.tell_hand_ranking() == '<Flush>':
            return 6
        elif self.tell_hand_ranking() == '<Straight>':
            return 5
        elif self.tell_hand_ranking() == '<Three of a kind>':
            return 4
        elif self.tell_hand_ranking() == '<Two pair>':
            return 3                    
        elif self.tell_hand_ranking() == '<One pair>':
            return 2
        elif self.tell_hand_ranking() == '<High card>':
            return 1
        else:
            return None
        
    #def compare(self,other):
        #if self.ranking_menu() > other.ranking_menu()
    
if __name__ == '__main__':
    import sys
    def test(did_pass):
        """  Print the result of a test.  """
        linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
        if did_pass:
            msg = "Test at line {0} ok.".format(linenum)
        else:
            msg = ("Test at line {0} FAILED.".format(linenum))
        print(msg)
my_hand = [('J', 'C'), ('Q', 'C'), ('A', 'C'), ('5', 'C'), ('6', 'C')]
your_hand = [('2', 'C'), ('4', 'C'), ('8', 'C'), ('9', 'C'), ('T', 'C')]
suits = 'CDHS'
ranks = '23456789TJQKA'
values = dict(zip(ranks, range(2, 2+len(ranks))))
my_hand.sort(key=lambda x: values[x[0]], reverse=True)
your_hand.sort(key=lambda x: values[x[0]], reverse=True)

    # your test cases here
    
h = Hands(my_hand)
yh = Hands(your_hand)
print('\t\tWhat is my cards?', my_hand, '\t\tWhat is your cards?', your_hand, sep='\n')
print('What is my Hand-ranking name?', h.tell_hand_ranking(), sep='\n')
print('What is your Hand-ranking name?', yh.tell_hand_ranking(), sep='\n')
print('Who wins the game?')


if (h.ranking_menu() > yh.ranking_menu()):
    print('***You WIN!***')
elif (h.ranking_menu() < yh.ranking_menu()):
    print('***You LOSE...***')
else:
    if (values[my_hand[0][0]] > values[your_hand[0][0]]):
        print('***You WIN!***')
    elif (values[my_hand[0][0]] < values[your_hand[0][0]]):
        print('***You LOSE...***')
    else:
        if(values[my_hand[1][0]] > values[your_hand[1][0]]):
            print('***You WIN!***')
        elif (values[my_hand[1][0]] < values[your_hand[1][0]]):
            print('***You LOSE...***') 
        else:
            if(values[my_hand[2][0]] > values[your_hand[2][0]]):
                print('***You WIN!***')
                
            elif (values[my_hand[1][0]] < values[your_hand[1][0]]):
                print('***You LOSE...***') 
            else:
                print('***DRAW...;;***') 
