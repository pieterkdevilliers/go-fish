
"""
Declare initial required lists to start the game, creating the full deck
and the empty hands for the two players.
"""
full_deck = [
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
            "Ace-Diamonds",
            "2-Diamonds",
            "3-Diamonds",
            "4-Diamonds",
            "5-Diamonds",
            "6-Diamonds",
            "7-Diamonds",
            "8-Diamonds",
            "9-Diamonds",
            "10-Diamonds",
            "Jack-Diamonds",
            "Queen-Diamonds",
            "King-Diamonds",
            "Ace-Clubs",
            "2-Clubs",
            "3-Clubs",
            "4-Clubs",
            "5-Clubs",
            "6-Clubs",
            "7-Clubs",
            "8-Clubs",
            "9-Clubs",
            "10-Clubs",
            "Jack-Clubs",
            "Queen-Clubs",
            "King-Clubs",
            "Ace-Spades",
            "2-Spades",
            "3-Spades",
            "4-Spades",
            "5-Spades",
            "6-Spades",
            "7-Spades",
            "8-Spades",
            "9-Spades",
            "10-Spades",
            "Jack-Spades",
            "Queen-Spades",
            "King-Spades"
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

    player_status = input("If you are ready to begine, type GO! below:\n")
    if player_status == "GO!":
        deal_cards()
    else:
        player_status = input("If you are ready to begine, type GO! below:\n")

def deal_cards():
    """
    Deals the cards by randomly selecting 7 cards for the Player and 7 cards for the computer.
    This will remove them from the full_deck list and add 7 cards to the player_hand
    list and 7 cards to the computer_hand list
    """
    print("cards are being dealt")


request_player_name()

explain_game_rules()
