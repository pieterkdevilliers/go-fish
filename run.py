# Importing required dependencies.

import random
import itertools
import time


# Declare initial required lists to start the game, creating the full deck
# and the card image reference.

CARD_IMAGES = {
    "Ace of Hearts": "Ace♥",
    "2 of Hearts": "2♥",
    "3 of Hearts": "3♥",
    "4 of Hearts": "4♥",
    "5 of Hearts": "5♥",
    "6 of Hearts": "6♥",
    "7 of Hearts": "7♥",
    "8 of Hearts": "8♥",
    "9 of Hearts": "9♥",
    "10 of Hearts": "10♥",
    "Jack of Hearts": "Jack♥",
    "Queen of Hearts": "Queen♥",
    "King of Hearts": "King♥",
    "Ace of Diamonds": "Ace♦",
    "2 of Diamonds": "2♦",
    "3 of Diamonds": "3♦",
    "4 of Diamonds": "4♦",
    "5 of Diamonds": "5♦",
    "6 of Diamonds": "6♦",
    "7 of Diamonds": "7♦",
    "8 of Diamonds": "8♦",
    "9 of Diamonds": "9♦",
    "10 of Diamonds": "10♦",
    "Jack of Diamonds": "Jack♦",
    "Queen of Diamonds": "Queen♦",
    "King of Diamonds": "King♦",
    "Ace of Clubs": "Ace♣",
    "2 of Clubs": "2♣",
    "3 of Clubs": "3♣",
    "4 of Clubs": "4♣",
    "5 of Clubs": "5♣",
    "6 of Clubs": "6♣",
    "7 of Clubs": "7♣",
    "8 of Clubs": "8♣",
    "9 of Clubs": "9♣",
    "10 of Clubs": "10♣",
    "Jack of Clubs": "Jack♣",
    "Queen of Clubs": "Queen♣",
    "King of Clubs": "King♣",
    "Ace of Spades": "Ace♠",
    "2 of Spades": "2♠",
    "3 of Spades": "3♠",
    "4 of Spades": "4♠",
    "5 of Spades": "5♠",
    "6 of Spades": "6♠",
    "7 of Spades": "7♠",
    "8 of Spades": "8♠",
    "9 of Spades": "9♠",
    "10 of Spades": "10♠",
    "Jack of Spades": "Jack♠",
    "Queen of Spades": "Queen♠",
    "King of Spades": "King♠"
}
initial_deck = [
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


class Game:
    """
    Runs the whole game.
    """
    def __init__(self, initial_deck):
        self.deck = initial_deck
        self.user_hand = []
        self.computer_hand = []
        self.user_foak = []
        self.computer_foak = []
        self.user_table = {}
        self.computer_table = {}

    def explain_game_rules(self):
        """
        Explain the rules of the game.
        """
        print("    __          __  _                           ")
        print("    \ \        / / | |                          ")
        print("     \ \  /\  / /__| | ___ ___  _ __ ___   ___  ")
        print("      \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \ ")
        print("       \  /\  /  __/ | (_| (_) | | | | | |  __/ ")
        print("        \/  \/ \   | |\___\___/| | | | | |\___| ")
        print("                                                ")
        time.sleep(2)
        print("Here are the rules of the game:\n")
        print("1 - The aim of the game is to end with the most Four Of A Kind")
        print("sets on the table and an empty hand.\n")
        print("2 - You and the computer will take turns in asking each other")
        print("for acard value. NOTE: You only request the card value,")
        print("NOT the card suit.\n")
        print("Example: If you want to know if the computer holds a 7,")
        print("you only request 7, not 7 of Hearts  or Queen and not")
        print("Queen of Diamonds etc...\n")
        print("3 - If the other player has the card requested, then it is")
        print("handed over and the player requests another card.\n")
        print("4 - If the other player does not have the requested card, the")
        print("active player draws a card from the deck,")
        print("and the other player has the next turn.\n")
        print("5 - The winner is the first player with an empty hand,")
        print("provided that player also has the highest number of")
        print("Four Of A Kind sets on the table.\n")
        self.start_game()

    def start_game(self):
        """
        Gets user to start the game, when ready.
        """
        player_status = input("If you are ready to begin, press ENTER:\n")
        if player_status == '':
            self.deal_cards()
        else:
            print("Command not recognised")
            self.start_game()

    def deal_cards(self):
        """
        Deals the cards by randomly selecting 7 cards for the user and 7 cards
        for the computer.
        This will remove them from the deck list and add 7 cards to the
        user hand list and 7 cards to the computer_hand list
        """
        print("\nCards are being dealt\n")
        time.sleep(2)

        i = 1
        while i <= 14:
            selected_card_position = random.randint(0, (len(self.deck) - 1))
            selected_card = self.deck[selected_card_position]
            self.deck.pop(int(selected_card_position))

            if i % 2 != 1:
                self.add_card_to_player_hand(selected_card, "user")
                i += 1
            
            else:
                self.add_card_to_player_hand(selected_card, "computer")
                i += 1

    def pull_card_from_deck(self):
        """
        Pulls a card from the deck to add it to the active user hand.
        """
        selected_card_position = random.randint(0, (len(self.deck) - 1))
        selected_card = self.deck[selected_card_position]
        self.deck.pop(int(selected_card_position))
        self.determine_pulled_card_value(selected_card)
        return selected_card

    def add_card_to_player_hand(self, selected_card, active_player):
        """
        Adds the selected card to the active_player's hand list.
        :param selected_card: The card selected from the deck EX: 3 of Hearts.
        :param active_player: The player who's turn it is, user or computer.
        """
        requested_card_value = (selected_card.split(maxsplit=1)[0])
        if active_player == "user":
            self.user_hand.append(selected_card)
        else:
            self.computer_hand.append(selected_card)
        return requested_card_value

    def select_next_card(self):
        """
        Identifies the next card to use out of the deck
        """
        selected_card_position = random.randint(0, (len(self.deck) - 1))
        selected_card = self.deck[selected_card_position]
        self.deck.pop(int(selected_card_position))
        return selected_card

    def play_a_round(self, active_player):
        """
        Determines if the opponent holds the requested card, and returns the
        card's index if True.
        :param active_player: The player who's turn it is, user or computer.
        """
        if active_player == "user":
            print("It is your turn.\n")
            print("You hold these cards in your hand:\n")
            self.user_hand.sort()
            for card in self.user_hand:
                print(CARD_IMAGES[card])
            requested_card = input("\nWhich card do you want to request?\n")
            self.validate_input(requested_card)
            card_check = any(card.startswith(
                requested_card) for card in self.computer_hand)
            if card_check is True:
                requested_card_index = len(tuple(itertools.takewhile(lambda x:
                    (requested_card) not in x, self.computer_hand)))
                requested_card = self.hand_over_requested_card(
                    requested_card_index, active_player)
                requested_card = self.add_card_to_player_hand(
                    requested_card, active_player)
                requested_card_value = self.check_player_hand_for_foak(
                    requested_card, active_player)
                self.confirm_player_foak(requested_card, active_player)
                self.user_foak.clear()

            else:
                if self.deck != []:
                    print("\nThe Computer doesn't have that card.")
                    print("You are taking another card from the deck\n")
                    time.sleep(2)
                    selected_card = self.pull_card_from_deck()
                    print(f"You pulled a {selected_card} from the deck")
                    time.sleep(2)
                    self.add_card_to_player_hand(selected_card, active_player)
                    requested_card = self.determine_pulled_card_value(
                        selected_card)
                    requested_card_value = self.check_player_hand_for_foak(
                        requested_card, active_player)
                    self.confirm_player_foak(requested_card_value,
                                             active_player)
                    active_player = self.switch_active_player(active_player)
                else:
                    print("\nThere are no more cards left in the deck.\n")

        else:
            requested_card = self.determine_computer_request_value()
            print("The Computer is choosing a card to request\n")
            time.sleep(2)
            print(f"The card requested by the computer was: {requested_card}")
            time.sleep(0.5)

            card_check = any(card.startswith(
                requested_card) for card in self.user_hand)

            if card_check is True:
                requested_card_index = len(tuple(itertools.takewhile(lambda x:
                                           (requested_card) not in x,
                                           self.user_hand)))
                requested_card = self.hand_over_requested_card(
                    requested_card_index, active_player)
                requested_card = self.add_card_to_player_hand(
                    requested_card, active_player)
                requested_card_value = self.check_player_hand_for_foak(
                    requested_card, active_player)
                self.confirm_player_foak(requested_card, active_player)
                self.computer_foak.clear()
                
            else:
                if self.deck != []:
                    print("\nYou didn't have that card.")
                    print("The computer is taking a card from the deck\n")
                    time.sleep(2)
                    selected_card = self.pull_card_from_deck()
                    self.add_card_to_player_hand(selected_card, active_player)
                    requested_card = self.determine_pulled_card_value(
                        selected_card)
                    requested_card_value = self.check_player_hand_for_foak(
                        requested_card, active_player)
                    self.confirm_player_foak(requested_card_value,
                                             active_player)
                    active_player = self.switch_active_player(active_player)
                else:
                    print("\nThere are no more cards left in the deck.\n")
        self.report_scores(active_player, requested_card_value)

    def validate_input(self, requested_card):
        """
        Receives the user input and validates it.
        :param requested_card: The input received from the user
        """
        valid_inputs = ["2",
                        "3",
                        "4",
                        "5",
                        "6",
                        "7",
                        "8",
                        "9",
                        "10",
                        "Jack",
                        "Queen",
                        "King",
                        "Ace"]
        if (requested_card.capitalize()) not in valid_inputs:
            print(requested_card.capitalize())
            print(f"{requested_card} is not a valid option. Choose again")
            requested_card = input("\nWhich card do you want to request?\n")
            self.validate_input(requested_card)
        else:
            return requested_card

    def hand_over_requested_card(self, requested_card_index, active_player):
        """
        Receives the requested card's index and removes it from the
        in_active player's hand.
        :param requested_card_index: The index of the requested card held
        by the opponent.
        :param active_player: The player who's turn it is, user or computer.
        """
        if active_player == "user":
            print("\nThe computer is handing over the card you requested\n")
            time.sleep(2)
            requested_card = self.computer_hand[requested_card_index]
            self.computer_hand.pop(int(requested_card_index))
        else:
            print("\nYou are handing over the card the Computer requested\n")
            time.sleep(2)
            requested_card = self.user_hand[requested_card_index]
            self.user_hand.pop(int(requested_card_index))
        return requested_card

    def switch_active_player(self, active_player):
        """
        Switches the active player beased on the existing
        active player, to change turns.
        :param active_player: The player who's turn it is, user or computer.
        """
        if active_player == "user":
            active_player = "computer"
            print("\nIt is now the Computer's turn")
            time.sleep(2)
            return active_player
        else:
            active_player = "user"
            return active_player

    def determine_computer_request_value(self):
        """
        Determines the card value the computer is asking the user for. 
        """
        computer_hand_len = len(self.computer_hand)
        if computer_hand_len != 1:
            computer_requested_card_position = random.randint(
                0, (computer_hand_len - 1))
            computer_requested_card = self.computer_hand[
                computer_requested_card_position]
        else:
            computer_requested_card = self.computer_hand[0]
        computer_request_value = computer_requested_card.split(maxsplit=1)
        return (computer_request_value[0])

    def determine_pulled_card_value(self, selected_card):
        """
        Determines the card value of the new card drawn from the deck.
        :param selected_card: The card selected from the deck EX: 3 of Hearts.
        """
        split_selected_card = selected_card.split(maxsplit=1)
        pulled_card_value = (split_selected_card[0])
        return pulled_card_value

    def check_player_hand_for_foak(self, requested_card, active_player):
        """
        Updates foak list with request card matches from player's
        hand and adds to the temp foak list.
        :param requested_card: Name and value of the card added to the player
        hand. Ex: 3 of Hearts.
        :param active_player: The player who's turn it is, user or computer.
        """
        requested_card_value = (requested_card.split(maxsplit=1)[0])
        if active_player == "user":
            for i, elem in enumerate(self.user_hand):
                if requested_card_value in elem:
                    self.user_foak.append(self.user_hand[i])
            return requested_card_value
        else:
            for i, elem in enumerate(self.computer_hand):
                if requested_card_value in elem:
                    self.computer_foak.append(self.computer_hand[i])
            return requested_card_value

    def confirm_player_foak(self, requested_card_value, active_player):
        """
        Determines if player foak is full, if so, adds foak list
        to table and clears foak.
        :param requested_card_value: The value of the card requested.
        Ex: 3 or King.
        :param active_player: The player who's turn it is, user or computer.
        """
        if active_player == "user":
            if len(self.user_foak) == 4:
                self.user_table[requested_card_value] = self.user_foak.copy()
                self.identify_foak_index_from_player_hand(
                    requested_card_value, active_player)
                self.user_foak.clear()
            else:
                self.user_foak.clear()
        else:
            if len(self.computer_foak) == 4:
                self.computer_table[requested_card_value] = self.computer_foak.copy()
                self.identify_foak_index_from_player_hand(
                    requested_card_value, active_player)
                self.computer_foak.clear()
            else:
                self.computer_foak.clear()

    def identify_foak_index_from_player_hand(self, requested_card_value,
                                             active_player):
        """
        Identifies and removes the foak cards from the player's hand
        after they were added to the player's table.
        :param requested_card_value: The value of the card requested.
        Ex: 3 or King.
        :param active_player: The player who's turn it is, user or computer.
        """
        if active_player == "user":
            for card in self.user_hand[:]:
                if requested_card_value in card:
                    foak_card_index = len(tuple(itertools.takewhile(lambda x: (
                        f"{requested_card_value}") not in x, self.user_hand)))
                    self.delete_foak_from_player_hand(foak_card_index,
                                                      active_player)
        else:
            for card in self.computer_hand[:]:
                if requested_card_value in card:

                    foak_card_index = len(tuple(itertools.takewhile(lambda x: (
                        f"{requested_card_value}") not in x, self.computer_hand)))
                    self.delete_foak_from_player_hand(foak_card_index,
                                                      active_player)

    def delete_foak_from_player_hand(self, foak_card_index, active_player):
        """
        Deletes identified foak card from player hand.
        :param foak_card_index: The index of the identified foak
        card to be removed from the players hand.
        :param active_player: The player who's turn it is, user or computer.
        """
        if active_player == "user":
            self.user_hand.pop(int(foak_card_index))
        else:
            self.computer_hand.pop(int(foak_card_index))

    def report_scores(self, active_player, requested_card_value):
        """
        Reports the scores for each player at the end of each round.
        This only happens once at least one player has a foak.
        :param user_table: The list holding the Four Of A Kind lists for the user.
        :param computer_table: The list holding the Four Of A Kind lists
        for the computer.
        :param deck: All the cards remaining in the deck.
        :param active_player: The player who's turn it is, user or computer.
        :param user_hand: The list of cards in the user's hand.
        :param computer_hand: The list of cards in the computer's hand.
        """
        if self.user_hand != [] and self.computer_hand != []:
            print("**********************  *********************\n")
            if len(self.user_table) != 0:
                print("\n")
                print("\n")
                print(f"You have {len(self.user_table)} on the table as Four Of A Kinds.\n")
                print("\n")
                print("Your Four Of A Kinds are:")
                for suit in self.user_table:
                    for card in self.user_table[suit]:
                        print(CARD_IMAGES[card])
                    print("**********************\n")

            if len(self.computer_table) != 0:
                print("\n")
                print("\n")
                time.sleep(2)
                print(f"The computer has {len(self.computer_table)} on the")
                print("table as it's Four Of A Kinds.\n")
                print("\n")
                print("The computer's Four Of A Kinds are:")
                for suit in self.computer_table:
                    for card in self.computer_table[suit]:
                        print(CARD_IMAGES[card])
                    print("**********************\n")

            self.play_a_round(active_player)
        else:
            self.determine_winner()

    def determine_winner(self):
        """
        Determines the winner once one player has an empty hand by counting and
        comparing the number of foak for each player.
        :param user_table: The list holding the Four Of A Kind lists for the
        user.
        :param computer_table: The list holding the Four Of A Kind lists
        for the computer.
        :param user_hand: The list of cards in the user's hand.
        :param computer_hand: The list of cards in the computer's hand.
        """
        user_table_len = len(self.user_table)
        computer_table_len = len(self.computer_table)
        if user_table_len > computer_table_len:
            print("\n")
            print("\n")
            print("You win!!")
            print("\n")
            print("\n")
            print(f"You have {user_table_len} four of a kinds and the")
            print(f"computer has {computer_table_len}.")

        elif computer_table_len > user_table_len:
            print("\n")
            print("\n")
            print("The computer won.")
            print("\n")
            print("\n")
            print(f"You have {user_table_len} four of a kinds and the")
            print(f"computer has {computer_table_len}.")
        else:
            print("\n")
            print("\n")
            print("Looks like it is a draw.")
            print("\n")
            print("\n")
            print(f"You have {user_table_len} four of a kinds and the")
            print(f"computer has {computer_table_len}.")
        self.play_another_round()

    def play_another_round(self):
        """
        Offers the player the chance to play again
        """
        print("Click the `Run Program` button to play again")


def main():
    """
    Runs the main functions of the game.
    """
    game = Game(initial_deck=initial_deck)
    game.explain_game_rules()
    print("\n")
    active_player = "user"
    game.play_a_round(active_player)


main()
