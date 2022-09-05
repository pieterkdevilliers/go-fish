# Importing required dependencies.

import random


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
player_hand = []
computer_hand = []

def request_player_name():
    """
    Requests the players name in order to start the game.
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
    Deals the cards by randomly selecting 7 cards for the Player and 7 cards for the computer.
    This will remove them from the deck list and add 7 cards to the player_hand
    list and 7 cards to the computer_hand list
    """
    print("\nCards are being dealt\n")
    print(f"Starting deck size is: {deck_size}")

    i = 1
    while i <= 14:
        selected_card_position = random.randint(0, (len(deck) - 1))
        selected_card = deck[selected_card_position]
        deck.pop(int(selected_card_position))

        if i % 2 != 1:
            add_card_to_player_hand(selected_card)
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

def add_card_to_player_hand(selected_card):
    """
    Adds the selected card to the player_hand list.
    """
    player_hand.append(selected_card)

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

def pull_cards_test(selected_card):
    """
    Allows for user selection of the next player, in order to test cards pulled from the deck.
    """
    while int(len(deck)) > 0:

        next_player = input("user or computer next?")

        if next_player == "user":
            print("You chose user as the next player")
            add_card_to_player_hand(pull_card_from_deck("user"))
            print(player_hand)

        elif next_player == "computer":
            print("You chose user as the next player")
            add_card_to_computer_hand(pull_card_from_deck("computer"))
            print(computer_hand)

        else:
            print("That is not an option")


def main():
    """
    Runs the main functions of the game.
    """

    request_player_name()
    explain_game_rules()
    print("\nThe cards in the player's hand:")
    print(player_hand)
    print("\n")
    print("The cards in the computer's hand:")
    print(computer_hand)
    print(len(deck))
    active_player = "user"
    print("\nCurrent Active Player:")
    print(active_player)

# Start main game running

main()

pull_cards_test(select_next_card())