# Importing required dependencies.

import random
import itertools
import re
import time


# Declare initial required lists to start the game, creating the full deck
# and the empty hands for the two players.


deck = [
            "Ace of Hearts",
            "2 of Hearts",
            "3 of Hearts",
            "4 of Hearts",
            "5 of Hearts",
            "6 of Hearts",
            "7 of Hearts",
            "8 of Hearts",
            "9 of Hearts",
            "10 of Hearts",
            "Jack of Hearts",
            "Queen of Hearts",
            "King of Hearts",
            "Ace of Diamonds",
            "2 of Diamonds",
            "3 of Diamonds",
            "4 of Diamonds",
            "5 of Diamonds",
            "6 of Diamonds",
            "7 of Diamonds",
            "8 of Diamonds",
            "9 of Diamonds",
            "10 of Diamonds",
            "Jack of Diamonds",
            "Queen of Diamonds",
            "King of Diamonds",
            "Ace of Clubs",
            "2 of Clubs",
            "3 of Clubs",
            "4 of Clubs",
            "5 of Clubs",
            "6 of Clubs",
            "7 of Clubs",
            "8 of Clubs",
            "9 of Clubs",
            "10 of Clubs",
            "Jack of Clubs",
            "Queen of Clubs",
            "King of Clubs",
            "Ace of Spades",
            "2 of Spades",
            "3 of Spades",
            "4 of Spades",
            "5 of Spades",
            "6 of Spades",
            "7 of Spades",
            "8 of Spades",
            "9 of Spades",
            "10 of Spades",
            "Jack of Spades",
            "Queen of Spades",
            "King of Spades"
            ]
user_hand = []
computer_hand = []
user_foak = []
computer_foak = []
user_table = {}
computer_table = {}


def request_player_name():
    """
    Requests the user's name in order to start the game.
    """
    while True:
        print("To start the game, please enter your name:\n")

        player_name = input("Enter your name:\n")
        print(f"Welcome {player_name}!\n")
        return player_name

def explain_game_rules():
    """
    Explain the rules of the game, and get user to start the game, when ready.
    """
    print("Here are the rules of the game:\n")
    print("Rule 1\n")
    print("Rule 2\n")
    print("Rule 3\n")

    player_status = input("If you are ready to begin, type GO! below:\n")
    if player_status == "GO!":
        count_cards_in_deck()
    else:
        player_status = input("That command is not recognised. In order to start the game type GO! below:\n")

def deal_cards(deck_size):
    """
    Deals the cards by randomly selecting 7 cards for the user and 7 cards for the computer.
    This will remove them from the deck list and add 7 cards to the user_hand
    list and 7 cards to the computer_hand list
    """
    print("\nCards are being dealt\n")
    time.sleep(2)

    i = 1
    while i <= 14:
        selected_card_position = random.randint(0, (len(deck) - 1))
        selected_card = deck[selected_card_position]
        deck.pop(int(selected_card_position))

        if i % 2 != 1:
            add_card_to_user_hand(selected_card)
            i += 1
        
        else:
            add_card_to_computer_hand(selected_card)
            i += 1

def pull_card_from_deck(active_player):
    """
    Pulls a card from the deck to add it to the active user hand.
    """
    selected_card_position = random.randint(0, (len(deck) - 1))
    selected_card = deck[selected_card_position]
    deck.pop(int(selected_card_position))
    determine_pulled_card_value(selected_card, active_player)
    return selected_card

def add_card_to_user_hand(selected_card):
    """
    Adds the selected card to the user_hand list.
    """
    user_hand.append(selected_card)

def add_card_to_computer_hand(selected_card):
    """
    Adds the selected card to the computer_hand list.
    """
    computer_hand.append(selected_card)


def count_cards_in_deck():
    """
    Checks remaining number of cards in deck, to determine the range of the random card select.
    """
    num_cards_in_deck = len(deck)
    deal_cards(num_cards_in_deck)

def select_next_card():
    """
    Identifies the next card to use out of the deck
    """
    selected_card_position = random.randint(0, (len(deck) - 1))
    selected_card = deck[selected_card_position]
    deck.pop(int(selected_card_position))
    return selected_card

def request_card(active_player):
    """
    Determines if the opponent holds the requested card, and returns the card's index if True.
    """
    if active_player == "User":
        print("It is your turn.\n")
        print("\n")
        print("You hold these cards in your hand:\n")
        print(user_hand)
        requested_card = input("\nWhich card do you want to request?\n")
        card_check = any(card.startswith(f"{requested_card}") for card in computer_hand)
        if card_check == True:
            requested_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card}") not in x, computer_hand)))
            hand_over_requested_card(requested_card_index, active_player)
            check_user_hand_for_foak(requested_card)
            user_foak.clear()
            request_card(active_player)
            
        else:
            print("\nThe Computer doesn't have that card, take another card from the deck\n")
            add_card_to_user_hand(pull_card_from_deck("user"))
            active_player = switch_active_player(active_player)
            request_card(active_player)
    else:
        requested_card = determine_computer_request_value()
        print("The Computer is choosing a card to request\n")
        time.sleep(2)
        print(f"The card requested by the computer was: {requested_card}")
        time.sleep(1)

        card_check = any(card.startswith(f"{requested_card}") for card in user_hand)

        if card_check == True:
            requested_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card}") not in x, user_hand)))
            hand_over_requested_card(requested_card_index, active_player)
            check_computer_hand_for_foak(requested_card)
            computer_foak.clear()
            request_card(active_player)
            
        else:
            print("\nYou didn't have that card, the computer is taking another card from the deck\n")
            time.sleep(1)
            add_card_to_computer_hand(pull_card_from_deck("computer"))
            active_player = switch_active_player(active_player)
            request_card(active_player)

def hand_over_requested_card(requested_card_index, active_player):
    """
    Receives the requested card's index and moves it from the computer_hand to the user_hand
    """
    if active_player == "User":
        print("\nThe computer is handing over the card you requested\n")
        time.sleep(1)
        requested_card = computer_hand[requested_card_index]
        computer_hand.pop(int(requested_card_index))
        add_card_to_user_hand(requested_card)
    else:
        print("\nYou are handing over the card the Computer requested\n")
        time.sleep(1)
        requested_card = user_hand[requested_card_index]
        user_hand.pop(int(requested_card_index))
        add_card_to_computer_hand(requested_card)

def switch_active_player(active_player):
    """
    Switches the active player beased on the existing active player, to change turns
    """
    if active_player == "User":
        active_player = "Computer"
        print("\nIt is now the Computer's turn")
        time.sleep(1)
        return active_player
    else:
        active_player = "User"
        return active_player

def determine_computer_request_value():
    """
    Determines the card value the computer is asking the user for. 
    """
    computer_requested_card_position = random.randint(0, (len(computer_hand) - 1))
    computer_requested_card = computer_hand[computer_requested_card_position]
    computer_request_value = computer_requested_card.split(maxsplit=1)
    return (computer_request_value[0])

def determine_pulled_card_value(selected_card, active_player):
    """
    Determines the card value of the new card drawn from the deck. 
    """
    pulled_card_value = selected_card.split(maxsplit=1)
    if active_player == "user":
        print("Checking the user hand for foak after pulling a card from deck")
        time.sleep(1)
        check_user_hand_for_foak(str(pulled_card_value))
    else:
        check_computer_hand_for_foak(str(pulled_card_value))
        print("Checking the computer hand for foak after pulling a card from deck")
        time.sleep(1)
    return (pulled_card_value[0])


def check_user_hand_for_foak(requested_card):
    """
    Updates foak list with request card matches from user's
    hand and adds to the temp foak list.
    """
    for i, elem in enumerate(user_hand):
        if requested_card in elem:
            user_foak.append(user_hand[i])     
    confirm_user_foak(requested_card)

def check_computer_hand_for_foak(requested_card):
    """
    Updates foak list with request card matches from computer's
    hand and adds to the temp foak list.
    """
    for i, elem in enumerate(computer_hand):
        if requested_card in elem:
            computer_foak.append(computer_hand[i])  
    confirm_computer_foak(requested_card)


def confirm_user_foak(requested_card):
    """
    Determines if user foak is full, if so, adds foak list to table and clears foak.
    """
    if len(user_foak) == 4:
        user_table[requested_card] = user_foak.copy()
        print("\nCongratulations! You have a Four Of A King\n")
        print("\nYour Four Of A Kinds Are:\n")
        print(user_table)
        delete_foak_from_user_hand(requested_card)
        user_foak.clear()
    else:
        user_foak.clear()

def delete_foak_from_user_hand(requested_card):
    """
    Identifies and removes the foak cards from the user_hand after they were added to the user_table
    """
    for i, elem in enumerate(user_hand):
        if requested_card in elem:
            print("Identifying foak user_hand index\n")
            time.sleep(1)
            foak_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card}") not in x, user_hand)))
            print(f"Deleting identified foak_index: {foak_card_index}")
            user_hand.pop(user_hand[(int(foak_card_index))])
            print("Deleting foak from user_hand\n")  

def confirm_computer_foak(requested_card):
    """
    Determines if computer foak is full, if so, adds foak list to table and clears foak.
    """
    if len(computer_foak) == 4:
        computer_table[requested_card] = computer_foak.copy()
        print("\nThe Computer has a Four Of A King\n")
        print("\nThe Computer's Four Of A Kinds Are:\n")
        print(computer_table)
        delete_foak_from_computer_hand(requested_card)
        computer_foak.clear()
    else:
        computer_foak.clear()

def delete_foak_from_computer_hand(requested_card):
    """
    Identifies and removes the foak cards from the computer_hand after they were added to the computer_table
    """
    for i, elem in enumerate(computer_hand):
        if requested_card in elem:
            print("Identifying foak computer_hand index\n")
            time.sleep(1)
            foak_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card}") not in x, computer_hand)))
            print(f"Deleting identified foak_index: {foak_card_index}")
            computer_hand.pop(computer_hand[(int(foak_card_index))])
            print("Deleting foak from computer_hand\n")   


def main():
    """
    Runs the main functions of the game.
    """
    request_player_name()
    explain_game_rules()
    print("\n")
    active_player = "User"
    request_card(active_player)

# Start main game running

main()
