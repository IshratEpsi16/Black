#-------BLACK JACK GAME---------#

#random numbers
import random
#computer cards
computer_cards = []
#player cards
player_cards = []
print("Welcome to BlackJack Game ")
print(' _________')
print('|         |')
print('|  BLACK  |')
print('|  JACK   |')
print('|         |')
print('|_________|')
print('Game Begin')
#computer cards
while len(computer_cards) !=2:      #if computer cards is less than 2
    computer_cards.append(random.randint(1,11))  
    if len(computer_cards) == 2:
        print("Computer has X & ",computer_cards[1])    # here computer's one card should be hidden and another 1 should displayed,let hidden one = 'X'

#player cards
while len(player_cards) !=2:      #if player cards is less than 2
    player_cards.append(random.randint(1,11))  
    if len(player_cards) == 2:
        print("You have  ",computer_cards)  #player's both card should be displayed
#sum of computer's card
if computer_cards == 21:
    print("Computer has 21 and Computer Wins !!")
elif sum(computer_cards) > 21:
    print("Computer has Busted !!")

#sum of player cards
while sum(player_cards) < 21:
    add_new=str(input("Do you want to hit or stand?\n")) #if player's total sum is not 21 or less than 21 he has a option to take more card by saying 'hit'
    if add_new == 'hit':
        player_cards.append(random.randint(1,11))
        print("Your sum is now " + str(sum(player_cards))+ " and these are ", player_cards)
    else:
        print("Computer's sum is " + str(sum(computer_cards))+ '  and these are ',computer_cards) 
        print("Your sum is now " + str(sum(player_cards))+ "  and these are ", player_cards)
        if sum(computer_cards) > sum(player_cards):
            print('Computer wins !! You lost')
            
        else:
            print('Congratulations !! You win')
            break
if sum(player_cards) > 21:
    print('You busted!! Computer wins')
elif sum(player_cards) == 21:
    print('Congratulations !! You have BlackJack and you win ')
    


