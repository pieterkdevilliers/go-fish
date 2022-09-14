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
        deal_cards()
    else:
        player_status = input("That command is not recognised. In order to start the game type GO! below:\n")


def deal_cards():
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
            add_card_to_player_hand(selected_card, "user")
            i += 1
        
        else:
            add_card_to_player_hand(selected_card, "computer")
            i += 1


def pull_card_from_deck():
    """
    Pulls a card from the deck to add it to the active user hand.
    """
    selected_card_position = random.randint(0, (len(deck) - 1))
    selected_card = deck[selected_card_position]
    deck.pop(int(selected_card_position))
    determine_pulled_card_value(selected_card)
    return selected_card


def add_card_to_player_hand(selected_card, active_player):
    """
    Adds the selected card to the active_player's hand list.
    """
    print(f"add_card_to_player_hand received: {selected_card} and {active_player}")
    requested_card_value = (selected_card.split(maxsplit=1)[0])
    if active_player == "user":
        user_hand.append(selected_card)
    else:
        computer_hand.append(selected_card)
    print(f"Value being returned by add_card_to_player_hand: {selected_card}")
    return requested_card_value


def select_next_card():
    """
    Identifies the next card to use out of the deck
    """
    selected_card_position = random.randint(0, (len(deck) - 1))
    selected_card = deck[selected_card_position]
    deck.pop(int(selected_card_position))
    return selected_card


def play_a_round(active_player):
    """
    Determines if the opponent holds the requested card, and returns the card's index if True.
    """
    if active_player == "user":
        print("It is your turn.\n")
        print("\n")
        print("You hold these cards in your hand:\n")
        print(user_hand)
        requested_card = input("\nWhich card do you want to request?\n")
        card_check = any(card.startswith(f"{requested_card}") for card in computer_hand)
        if card_check is True:
            requested_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card}") not in x, computer_hand)))
            requested_card = hand_over_requested_card(requested_card_index, active_player)
            requested_card = add_card_to_player_hand(requested_card, active_player)
            requested_card_value = check_player_hand_for_foak(requested_card, active_player)
            confirm_player_foak(requested_card, active_player)
            user_foak.clear()
            # report_scores(user_table, computer_table, deck)
            # play_a_round(active_player)
            
        else:
            if deck != []:
                print("\nThe Computer doesn't have that card, take another card from the deck\n")
                selected_card = pull_card_from_deck()
                add_card_to_player_hand(selected_card, active_player)
                requested_card = determine_pulled_card_value(selected_card)
                requested_card_value = check_player_hand_for_foak(requested_card, active_player)
                confirm_player_foak(requested_card_value, active_player)
                active_player = switch_active_player(active_player)
            else:
                print("\nThere are no more cards left in the deck.\n")
            # report_scores(user_table, computer_table, deck)
            # play_a_round(active_player) 

    else:
        requested_card = determine_computer_request_value()
        print("The Computer is choosing a card to request\n")
        time.sleep(2)
        print(f"The card requested by the computer was: {requested_card}")
        time.sleep(0.5)

        card_check = any(card.startswith(f"{requested_card}") for card in user_hand)

        if card_check is True:
            requested_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card}") not in x, user_hand)))
            requested_card = hand_over_requested_card(requested_card_index, active_player)
            requested_card = add_card_to_player_hand(requested_card, active_player)
            requested_card_value = check_player_hand_for_foak(requested_card, active_player)
            confirm_player_foak(requested_card, active_player)
            computer_foak.clear()  
            # report_scores(user_table, computer_table, deck)
            # play_a_round(active_player)
            
        else:
            if deck != []:
                print("\nYou didn't have that card, the computer is taking another card from the deck\n")
                time.sleep(0.5)
                selected_card = pull_card_from_deck()
                add_card_to_player_hand(selected_card, active_player)
                requested_card = determine_pulled_card_value(selected_card)
                requested_card_value = check_player_hand_for_foak(requested_card, active_player)
                confirm_player_foak(requested_card_value, active_player)
                active_player = switch_active_player(active_player)
            else:
                print("\nThere are no more cards left in the deck.\n")
            # report_scores(user_table, computer_table, deck)
            # play_a_round(active_player)
    report_scores(user_table, computer_table, deck, active_player)
            

def hand_over_requested_card(requested_card_index, active_player):
    """
    Receives the requested card's index and removes it from the in_active player's hand
    """
    if active_player == "user":
        print("\nThe computer is handing over the card you requested\n")
        time.sleep(0.5)
        requested_card = computer_hand[requested_card_index]
        computer_hand.pop(int(requested_card_index))
    else:
        print("\nYou are handing over the card the Computer requested\n")
        time.sleep(0.5)
        requested_card = user_hand[requested_card_index]
        user_hand.pop(int(requested_card_index))
    return requested_card


def switch_active_player(active_player):
    """
    Switches the active player beased on the existing active player, to change turns
    """
    if active_player == "user":
        active_player = "computer"
        print("\nIt is now the Computer's turn")
        time.sleep(0.5)
        return active_player
    else:
        active_player = "user"
        return active_player


def determine_computer_request_value():
    """
    Determines the card value the computer is asking the user for. 
    """
    if len(computer_hand) != 1:
        computer_requested_card_position = random.randint(0, (len(computer_hand) - 1))
        computer_requested_card = computer_hand[computer_requested_card_position]
    else:
        computer_requested_card = computer_hand[0]
    computer_request_value = computer_requested_card.split(maxsplit=1)
    return (computer_request_value[0])


def determine_pulled_card_value(selected_card):
    """
    Determines the card value of the new card drawn from the deck. 
    """
    split_selected_card = selected_card.split(maxsplit=1)
    pulled_card_value = (split_selected_card[0])
    return pulled_card_value


def check_player_hand_for_foak(requested_card, active_player):
    """
    Updates foak list with request card matches from player's
    hand and adds to the temp foak list.
    """
    requested_card_value = (requested_card.split(maxsplit=1)[0])
    if active_player == "user":
        for i, elem in enumerate(user_hand):
            if requested_card_value in elem:
                user_foak.append(user_hand[i])
        print(user_foak)
        return requested_card_value
    else:
        for i, elem in enumerate(computer_hand):
            if requested_card_value in elem:
                computer_foak.append(computer_hand[i])
        print(computer_foak)
        return requested_card_value


def confirm_player_foak(requested_card_value, active_player):
    """
    Determines if player foak is full, if so, adds foak list to table and clears foak.
    """
    if active_player == "user":
        if len(user_foak) == 4:
            user_table[requested_card_value] = user_foak.copy()
            print("\nCongratulations! You have a Four Of A Kind\n")
            print("\nYour Four Of A Kinds Are:\n")
            print(user_table)
            identify_foak_index_from_player_hand(requested_card_value, active_player)
            user_foak.clear()
        else:
            user_foak.clear()
    else:
        if len(computer_foak) == 4:
            computer_table[requested_card_value] = computer_foak.copy()
            print("\nThe Computer has a Four Of A Kind\n")
            print("\nThe Computer's Four Of A Kinds Are:\n")
            print(computer_table)
            identify_foak_index_from_player_hand(requested_card_value, active_player)
            computer_foak.clear()
        else:
            computer_foak.clear()


def identify_foak_index_from_player_hand(requested_card_value, active_player):
    """
    Identifies and removes the foak cards from the player's hand after they were added to the player's table
    """
    if active_player == "user":
        for card in user_hand[:]:
            if requested_card_value in card:
                foak_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card_value}") not in x, user_hand)))
                delete_foak_from_player_hand(foak_card_index, active_player)
    else:
        for card in computer_hand[:]:
            if requested_card_value in card:

                foak_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card_value}") not in x, computer_hand)))
                delete_foak_from_player_hand(foak_card_index, active_player)


def delete_foak_from_player_hand(foak_card_index, active_player):
    """
    Deletes identified foak card from player hand
    """
    if active_player == "user":
        user_hand.pop(int(foak_card_index))
    else:
        computer_hand.pop(int(foak_card_index))          


def report_scores(user_table, computer_table, deck, active_player, user_hand, computer_hand):
    """
    Reports the scores for each player at the end of each round. This only happens once at least one player has a foak.
    """
    if user_hand != [] and computer_hand != []:
        if len(user_table) != 0:
            print(f"You have {len(user_table)} on the table as Four Of A Kinds.\n")
            print("Your Four Of A Kinds are:")
            print(user_table)
            print("\n")
            print(f"The computer has {len(user_table)} on the table as it's Four Of A Kinds.\n")
            print("The computer's Four Of A Kinds are:")
            print(computer_table)

        play_a_round(active_player)
    else:
        determine_winner(user_table, user_hand, computer_table, computer_hand)


def determine_winner(user_table, user_hand, computer_table, computer_hand):
    """
    Determines the winner once one player has an empty hand by counting and comparing the number of foak for each player.
    """
    if len(user_table) > len(computer_table):
        print("You win!!")
        print(f"You have {len(user_table)} four of a kinds and the computer has {len(computer_table)}.")

    elif len(computer_table) > len(user_table):
        print("The computer won.")
        print(f"You have {len(user_table)} four of a kinds and the computer has {len(computer_table)}.")
    else:
        print("Looks like it is a draw.")
        print(f"You have {len(user_table)} four of a kinds and the computer has {len(computer_table)}.")


def main():
    """
    Runs the main functions of the game.
    """
    request_player_name()
    explain_game_rules()
    print("\n")
    active_player = "user"
    play_a_round(active_player)

# Start main game running

main()