#global variable
import random
suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11} #dictionary
playing=True
class Card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+' of '+self.suit

class Deck():
    def __init__(self):             
        self.deck=[]        #start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=' '
        for card in self.deck:
            deck_comp +='\n'+ card.__str__()
        return "The deck has : "+deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        single_card=self.deck.pop()
        return single_card
#
#test_deck=Deck()
#test_deck.shuffle()
#print(test_deck)
class Hand():   
    def __init__(self):
        self.cards=[]               #start with an empty list as we did in the deck class
        self.value=0                #start with 0 value
        self.aces=0                 #add an attribute to keep track of aces
    def add_card(self,card):
        #card passed in
        #from Deck.deal() -->single Card(suit,rank)
        self.cards.append(card)
        self.value +=values[card.rank]
        #track aces
        if card.rank == 'Ace':
            self.aces +=1
    def adjust_for_ace(self):
        #if total value >21 and i still have an ace
        #than change my ace to be a 1 instead of an 11
        while self.value >21 and self.aces>0:
            self.value -=10
            self.aces -= 1
           
#zero=0
#one=1
#two=2
#if 2:
    #print('True')
test_deck=Deck()
test_deck.shuffle()
#player
test_player=Hand()
#deal 1 card from the deck Card(suit,rank)
pulled_card=test_deck.deal()
#print(pulled_card)
test_player.add_card(pulled_card)
#print(test_player.value)
test_player.add_card(test_deck.deal())
#print(test_player.value)
class Chips:
    def __init__(self,total=100):
        self.total=total        #this can be set to a default value or suplied by a user input
        self.bet=0
    def win_bet(self):
        self.total +=self.bet
    def lose_bet(self):
        self.total -=self.bet
def take_bet(chips):
    while True:
        try:
            
            chips.bet=int(input('How many chips would you like to bet : '))
        except:
            print('Please provide an integer')
        else:
            if chips.bet>chips.total:
                print('Sorry you do not have enough chips! You have : {} '.format(chips.total))

            else:
                break
def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
def hit_or_stand(deck,hand):
    global playing      # to control an upcoming while loop
    while True:
        x=input('Hit or Stand?Enter h or s ')       #HIT ##hh #stand
        if x[0].lower()=='h':
            hit(deck,hand)
        elif x[0].lower()=='s':
            print("Player Stands Dealer's turn ")
                
            playing=False
         
            
            
            
        else:
            print("Sorry,I did not understand that,please enter h or s only!")
            continue
        break
def show_some(player,dealer):
    print("Dealers HAND : ")
    print("One card hidden!")
    print(dealer.cards[1])
    print('\n')
    print('Players Hand:')
    for card in player.cards:
        print(card)
def show_all(player,dealer):
    print("Dealers HAND : ")
    for card in dealer.cards:
        print(card)
        print('\n')
        print('Players Hand:')
        for card in player.cards:
            print(card)
        
def player_busts(player,dealer,chips):
    print("Bust Player!")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("Player Wins!")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("Player wins!Dealer busted")
    chips.win_bet()
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
def push(player,dealer):
    print('Dealer and player ties!PUSH')

while True:
    #print an opening statement
    print("Welcome to BlackJack ")
    print(' _________')
    print('|         |')
    print('|  BLACK  |')
    print('|  JACK   |')
    print('|         |')
    print('|_________|')
        #create and shufflethe deck,deal two cards to each player
    deck=Deck()
    deck.shuffle()
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    #set up the player chips
    player_chips=Chips()
    #prompt the player for their bet
    take_bet(player_chips)
    #show cards (but keep 1 dealer card hidden)
    show_some(player_hand,dealer_hand)
    while playing:  #recallthis variable from our hit_or_stand function
        #prompt for player to hit or stand
        hit_or_stand(deck,player_hand) 
        #show cards(but keep 1 dealer card hidden)
        show_some(player_hand,dealer_hand)
        #if player hand excceds 21,run players_bust()& break out of loop
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        #if player hasn't busted ,play dealer's hand untill dealer reaches 17
    if player_hand.value<=21:
        while dealer_hand.value<17:
            hit(deck,dealer_hand)
        #show all cards
        show_all(player_hand,dealer_hand)
        #run different wining scenarious

        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        #inform player of their chips total
    print('\n Player total chips are at : {}'.format(player_chips.total))
    #ask to play again
    new_game=input("Would you like to play another hand? y/n")
    if new_game[0].lower()=='y':
        playing = True
        continue
    else:
        print('Thank you for playing')
        break

                    














