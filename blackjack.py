'''
This program runs a game of blackjack completely in the terminal.
It can be played for fun by any user, and it is a great way to pass time or have fun with friends.
It can also help gambling addicts by gambling with vitual money instead of real money.

Game by Soutine/iodineschool for AP CSP
'''

import random
import time

# Fresh deck of cards, untouched
fresh_deck = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10]

# The main attraction, defines the blackjack game
def blackjack(round_number, total_money):
    print(f""" 
 --------------------------------
|                                |
|     Welcome to Blackjack!      |
|                                |
 --------------------------------
You have ${total_money} to start with.
The dealer has the same amount. Game goes until you or the dealer runs out of money.
""") # Fancy title, displays the player's starting money
    player_money = total_money # Sets the player's money to the total money
    dealer_money = total_money # Sets the dealer's money to the total money

    # Main game loop
    while True:
        time.sleep(2) # Pauses for 2 seconds
        print(f"It is currently round {round_number}.") # Displays the number of the current round
        round_number = round_number + 1 # Increases the round number by 1

    # Asks the player how much they would like to bet, and checks if the bet is valid
        while True:
            try:
                player_bet = int(input("How much would you like to bet? "))
                if player_bet <= 0:
                    raise ValueError("Bet must be greater than 0. Please enter a valid bet.")
                if player_bet > player_money:
                    raise ValueError("You don't have enough money to bet that much. Please enter a valid bet.")
                if player_bet > dealer_money:
                    raise ValueError("The dealer doesn't have enough money to bet that much. Please enter a valid bet.")
                break
            except ValueError as uwu:
                print(f"{uwu}") # uwu
        print(f"You have made a bet of ${player_bet}.") # Displays the player's bet

        # Deal initial hands
        deck = fresh_deck.copy() # Copies the fresh deck
        random.shuffle(deck) # Deck is shuffled
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Defines variables for the stand trackers to use in the round
        player_stand_tracker = 0
        dealer_stand_tracker = 0
        stand_tracker = 0

        # Completes a round
        while True:

            # Adds up the hands
            dealer_total = sum(dealer_hand)
            player_total = sum(player_hand)

            time.sleep(2) # Pauses for 2 seconds
            print(f"""
--------------------------------

Dealer's hand: {dealer_hand[1:]} + Hidden Card

Your hand: {player_hand}
Hand total: {player_total}

-------------------------------- 
                  """) # Fancy display of the dealer's hand and the player's hand
            
            # Player's turn
            while player_total <= 21:
                if len(player_hand) == 5: # If player has 5 cards, they cannot perform an action
                    print("You have 5 cards! You cannot perform an action.")
                    time.sleep(2) # Pauses for 2 seconds
                    break
                if player_stand_tracker == 1: # If player stood last round, they cannot perform an action
                    print("You stood last round! You cannot perform an action.")
                    time.sleep(2) # Pauses for 2 seconds
                    break
                player_action = input("Would you like to hit or stand? ").lower()
                if player_action == "hit":
                    print("You hit!")
                    player_hand.append(deck.pop())
                    break
                elif player_action == "stand":
                    print("You stand!")
                    player_stand_tracker = 1
                    break
                else:
                    print("Please enter a valid action.") # Error check

            # Dealer's turn
            if dealer_total < 17:
                print("Dealer hits!")
                dealer_hand.append(deck.pop())
                dealer_total = sum(dealer_hand)
            else:
                print("Dealer stands!")
                dealer_stand_tracker = 1

            # If both the player and the dealer stand, sets stand tracker to 1, which ends the round
            if player_stand_tracker == 1 and dealer_stand_tracker == 1:
                stand_tracker = 1

            # Determines if there is a winner
            if player_total > 21:
                print("You bust! Dealer wins.")
                player_money -= player_bet
                dealer_money += player_bet
                break
            elif dealer_total > 21:
                print("Dealer busts! You win.")
                player_money += player_bet
                dealer_money -= player_bet
                break
            elif stand_tracker == 1 and player_total > dealer_total:
                print("You win!")
                player_money += player_bet
                dealer_money -= player_bet
                break
            elif stand_tracker == 1 and player_total < dealer_total:
                print("Dealer wins!")
                player_money -= player_bet
                dealer_money += player_bet
                break
            elif player_total == dealer_total:
                print("It's a tie! No one wins.")
                break
            else:
                continue
        time.sleep(2) # Pauses for 2 seconds
        print(f"""

-------------------------------- 
              
Round over. You have {player_money} left, and the dealer has {dealer_money} left.

-------------------------------- 
""") # Displays the player's money and the dealer's money

        if player_money == 0:
            print(f"""
 -------------------------------
|                               |
|   You have run out of money!  |
|       The dealer wins!        |
|                               |
 -------------------------------
""") # Fancy dealer win display
            break
        if dealer_money == 0:
            print(f"""
 ----------------------------------
|                                  |
|   The dealer ran out of money!   |
|           You win!               |
|                                  |
 ----------------------------------
""") # Fancy player win display
            break


# Runs the blackjack game starting on round 1 with $1,000,000
blackjack(1, 1000000)