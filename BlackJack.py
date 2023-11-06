import random
import os
import time

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for i in suits:
            for j in ranks:
                self.all_cards.append(Card(i, j))
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal(self):
        return self.all_cards.pop()
    
def total(hand):
    total = 0
    hand_ranks = []
    for i in hand.cards:
        hand_ranks.append(i.rank)
        total += values[i.rank]
        
    if ranks[12] in hand_ranks and total > 21:
        total = total - 10
        
    return total

def burst(hand):
    
    if total(hand) > 21:
        return True
    else:
        return False
    
class Hand:
    def __init__(self):
        self.cards = []
    
    def add_cards(self, card):
        self.cards.append(card)
    def print_hand(self):
        print(*self.cards, sep="..")

class Chips:
    
    def __init__(self, total = 100):
        
        self.total = total
        self.bet = 0
        
    def win_bet(self, bet):
        self.total += 2* (self.bet)
        
    def lose_bet(self, bet):
        self.total = self.total
    def tie_bet(self, bet):
        self.total += self.bet


def take_bet(chips):

    while True:
        if chips.total <= 0:
            print("You don't have sufficient amount to make bets")
            return 0
        else:
            print(f"You have {chips.total} chips remaining\n")
            print("How much would you like to bet. sir?\n")
            words("You can bet as much as you want\n\nHALF.... FULL.... or Your Choice\n\n ")
            time.sleep(1)
            print("YOUR CALL sir..!!")
            choice = input("-->")
            try:
                int(choice)
            except:
                if choice[0].lower() == "h":
                    given = int(chips.total/2)
                    if given > 0:
                        chips.total = chips.total/2
                    else:
                        continue


                elif choice[0].lower() == "f" or choice[0].lower() == "a":
                    given = int(chips.total)
                    if given > 0:
                        chips.total = 0
                    else:
                        continue

                
                elif choice[0].lower() != "h" or choice[0].lower() == "f":
                    continue
                return given

            else:
                given = chips.total - int(choice)
                if given >= 0:
                    chips.total = chips.total - int(choice)
                else:
                    continue
                
                return int(choice)


def raise_bet(chips, bet):
    while True:
        dec = input("\n\nDo you want to raise your bet sir..??-->")
        if dec[0].lower() != "y":
            break
        else:
            dec2 = int(input("How much sir -->"))
            given = chips.total - int(dec2)
            if given >= 0:
                chips.total = chips.total - int(dec2)
            else:
                continue
                
            return int(bet + int(dec2))            

def hit_or_stay(hand, deck):
    while True:
        time.sleep(1)
        os.system("clear")
        print("Your hand-->")
        hand.print_hand()
        print(f"\nYour total point is {total(hand)}")
        dec = input("\nDo you want to hit or stay\n-->")
        if dec[0].lower() == 'h':
            card = deck.deal()
            hand.add_cards(card)
            print(f"{card}..... has been added to your hand")
            if burst(hand) == True:
                print("BUSTED.......!!!!!!!")
                print(f"\nYour total point is {total(hand)}")
                break
            continue
            
        elif  dec[0].lower() == 's':
            break
            
        else:
            continue
            
        
def show_some(player, dealer):
    print("Player's Hand....")
    player.print_hand()
    print(f"player points ---->{total(player)}")
    print("\n\nDealer's Hand....")
    print("Hidden Card..", end="")
    for i in dealer.cards[1:]:
        print(i, end="..")
        
def show_all(player, dealer):
    print("Player's Hand....")
    player.print_hand()
    print("\n\nDealer's Hand....")
    dealer.print_hand()


def spark(Congratulations):    
    s = Congratulations
    for i in range(5):
        os.system("clear")
        print(s,end="")
        time.sleep(1)
    print("..!!")

def words(s):    
    for i in s.split():
        time.sleep(0.5)
        print(i, end=" ")



### Main game Logic

print("Hello sir,\n")
words("This is a BlackJack table")
time.sleep(1)
print("\nPlease sit down..\n\n")
time.sleep(2)

c = int(input("How much chips do you want to begin with?-->"))

player_chips = Chips(c)

while True:
    os.system("clear")
    deck = Deck()

    player = Hand()
    dealer = Hand()
    deck.shuffle()
    player_chips.bet = 0
    #print("Are you ready. please take a card")
    player.add_cards(deck.deal())
    #print("\nI am taking a card. and let's start...\n\n")
    dealer.add_cards(deck.deal())

    player_chips.bet = take_bet(player_chips)
    if player_chips.bet == 0:
        print("Good bye. sir")
        break
    
    print("\n\n")

    
    hit_or_stay(player, deck)
    player.print_hand()
    print("\n")
    words("Now i am taking some cards")
    words(". . . . ")
    print("DONE")
    time.sleep(2)
    os.system("clear")
    words("Let's show our cards")
    print("\n")
    print("\n")
    time.sleep(1)
 
    while total(dealer) < 18:
        dealer.add_cards(deck.deal())
        time.sleep(1)
    
    if burst(player) == True:
        spark(f"You busted..{total(player)}")
        print("You Lost")
        player_chips.lose_bet(player_chips.bet)
        
        
    elif burst(dealer) == True:
        spark(f"dealer busted..{total(dealer)}")
        print("Aawww. i busted..\nCongratulations sir. You win")
        player_chips.win_bet(player_chips.bet)
        
    else:
        show_some(player, dealer)
        if player_chips.total > 0:
            player_chips.bet = raise_bet(player_chips, player_chips.bet)
        show_all(player, dealer)
        
        if total(player) < total(dealer):
            spark("You lost..")
            print("Sorry sir. You lost")
            player_chips.lose_bet(player_chips.bet)
        elif total(player) > total(dealer):
            spark("Congratulations")
            print("Congratulation sir. You win")
            player_chips.win_bet(player_chips.bet)
        else:
            spark("PUSH")
            print("It's push")
            player_chips.tie_bet(player_chips.bet)
            
    show_all(player, dealer)
    print(f"\n\nPlayer points --> {total(player)}")
    print(f"\nDealer points --> {total(dealer)}")
    
    print(f"\nremaining chips are {player_chips.total}")
    while True:
        dec = input("Do you want to another round..??")
        if dec[0].lower() == "y" or dec[0].lower() == "n":
            break
        else:
            pass
    if dec[0].lower() == "y":
        continue
    else:
        os.system("clear")
        print("Good bye. sir..!!😇")

        words(f"You're walking away with {player_chips.total} chips")
        break
    