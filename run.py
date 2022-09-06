# Importing required dependencies.

import random
import itertools


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
    print(len(deck))
    print(f"Selected card from pull card function was {selected_card}")
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
        print("\nThe cards in the computer's hand:")
        print(computer_hand)
        requested_card = input("\nWhich card do you want to request?(You are playing as the USER)\n")
        print(requested_card)

        card_check = any(card.startswith(f"{requested_card}") for card in computer_hand)
        print(card_check)

        if card_check == True:
            requested_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card}") not in x, computer_hand)))
            print(requested_card_index)
            hand_over_requested_card(requested_card_index, active_player)
            request_card(active_player)
            
        else:
            print("I don't have that card, take another card from the deck")
            add_card_to_user_hand(pull_card_from_deck("user"))
            print(user_hand)
            active_player = switch_active_player(active_player)
            request_card(active_player)
    else:
        print("\nThe cards in the user's hand:")
        print(user_hand)
        # requested_card = input("\nWhich card do you want to request?(You are playing as the COMPUTER)\n")
        requested_card = determine_computer_request_value()
        print(f"The card requested by the computer was: {requested_card}")

        card_check = any(card.startswith(f"{requested_card}") for card in user_hand)
        print(card_check)

        if card_check == True:
            requested_card_index = len(tuple(itertools.takewhile(lambda x: (f"{requested_card}") not in x, user_hand)))
            print(requested_card_index)
            hand_over_requested_card(requested_card_index, active_player)
            request_card(active_player)
            
        else:
            print("I don't have that card, take another card from the deck")
            add_card_to_computer_hand(pull_card_from_deck("computer"))
            print(computer_hand)
            active_player = switch_active_player(active_player)
            request_card(active_player)

def hand_over_requested_card(requested_card_index, active_player):
    """
    Receives the requested card's index and moves it from the computer_hand to the user_hand
    """
    if active_player == "User":
        requested_card = computer_hand[requested_card_index]
        computer_hand.pop(int(requested_card_index))
        add_card_to_user_hand(requested_card)
        print("The cards in the computer's hand:")
        print(computer_hand)
        print("\nThe cards in the user's hand:")
        print(user_hand)
    else:
        requested_card = user_hand[requested_card_index]
        user_hand.pop(int(requested_card_index))
        add_card_to_computer_hand(requested_card)
        print("The cards in the computer's hand:")
        print(computer_hand)
        print("\nThe cards in the user's hand:")
        print(user_hand)

def switch_active_player(active_player):
    """
    Switches the active player beased on the existing active player, to change turns
    """
    if active_player == "User":
        active_player = "Computer"
        print(active_player)
        return active_player
    else:
        active_player = "User"
        print(active_player)
        return active_player

def determine_computer_request_value():
    """
    Determines the card value the computer is asking the user for. 
    """
    computer_requested_card_position = random.randint(0, (len(computer_hand) - 1))
    computer_requested_card = computer_hand[computer_requested_card_position]
    computer_request_value = computer_requested_card.split(maxsplit=1)
    return (computer_request_value[0])


def main():
    """
    Runs the main functions of the game.
    """
    request_player_name()
    explain_game_rules()
    print("\n")
    active_player = "User"
    print("\nCurrent Active Player is:")
    print(active_player)
    request_card(active_player)

# Start main game running

# main()

def 
user_hand = ["2 of hearts", "2 of Diamonds", "2 of Clubs", "2 of Spades", "6 of hearts", "5 of Diamonds", "4 of Clubs", "3 of Spades"]
user_foak = []
user_table = []

user_foak.append(user_hand[0])
print(user_foak)
user_foak.append(user_hand[1])
print(user_foak)
user_table.append(user_foak)
print(user_table)
print(user_table[0])
