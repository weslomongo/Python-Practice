import random


def create_deck():

    suits = ["♥️", "💎", "♣️", "♠️"]

    ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11
    }

    deck = []

    for suit in suits:
        for rank, value in ranks.items():

            card = {
                "rank": rank,
                "suit": suit,
                "value": value
            }

            deck.append(card)

    return deck


def deal_card(deck):
    return deck.pop()


def calculate_hand(hand):

    total = 0
    aces = 0

    for card in hand:

        total += card["value"]

        if card["rank"] == "Ace":
            aces += 1

    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


def display_hand(hand):

    for card in hand:
        print(f"{card['rank']} of {card['suit']}")


def player_turn(deck, player_hand):

    while True:

        print("\nYour hand:")
        display_hand(player_hand)

        player_total = calculate_hand(player_hand)

        print(f"Total: {player_total}")

        if player_total > 21:
            print("\nYou busted!")
            return

        if player_total == 21:
            print("\nYou have 21!")
            return

        choice = input("\nHit or stand? ").lower()

        if choice == "hit":

            new_card = deal_card(deck)

            player_hand.append(new_card)

            print(
                f"\nYou drew: "
                f"{new_card['rank']} of {new_card['suit']}"
            )

        elif choice == "stand":
            return

        else:
            print("Please type 'hit' or 'stand'.")


def dealer_turn(deck, dealer_hand):

    print("\nDealer's turn...")

    while calculate_hand(dealer_hand) < 17:

        new_card = deal_card(deck)

        dealer_hand.append(new_card)

        print(
            f"Dealer draws: "
            f"{new_card['rank']} of {new_card['suit']}"
        )

    dealer_total = calculate_hand(dealer_hand)

    if dealer_total > 21:
        print("Dealer busted!")

    else:
        print(f"Dealer stands at {dealer_total}")


def determine_winner(player_hand, dealer_hand):

    player_total = calculate_hand(player_hand)
    dealer_total = calculate_hand(dealer_hand)

    print("\n-----------------------")
    print("FINAL RESULTS")
    print("-----------------------")

    print("\nYour hand:")
    display_hand(player_hand)
    print(f"Total: {player_total}")

    print("\nDealer's hand:")
    display_hand(dealer_hand)
    print(f"Total: {dealer_total}")

    print()

    if player_total > 21:
        print("Dealer wins.")

    elif dealer_total > 21:
        print("You win!")

    elif player_total > dealer_total:
        print("You win!")

    elif dealer_total > player_total:
        print("Dealer wins.")

    else:
        print("Push! It's a tie.")


def play_blackjack():

    deck = create_deck()

    random.shuffle(deck)

    player_hand = []
    dealer_hand = []

    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))

    player_hand.append(deal_card(deck))
    dealer_hand.append(deal_card(deck))

    print("\n=======================")
    print("       BLACKJACK")
    print("=======================")

    print("\nDealer shows:")

    print(
        f"{dealer_hand[0]['rank']} "
        f"of {dealer_hand[0]['suit']}"
    )

    player_turn(deck, player_hand)

    if calculate_hand(player_hand) <= 21:
        dealer_turn(deck, dealer_hand)

    determine_winner(player_hand, dealer_hand)


while True:

    play_blackjack()

    again = input("\nPlay again? (yes or no): ").lower()

    if again != "yes":
        print("Thanks for playing!")
        break