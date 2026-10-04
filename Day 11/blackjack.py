import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(cards)


def calculate_score(hand):
    """Return the hand's score, counting an Ace as 1 if 11 would bust."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, the dealer has Blackjack"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "The dealer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose"


def play_game():
    user_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]
    game_over = False

    while not game_over:
        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)
        print(f"Your cards: {user_hand}, score: {user_score}")
        print(f"Dealer's first card: {computer_hand[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        elif input("Type 'y' to get another card, 'n' to pass: ").lower() == "y":
            user_hand.append(deal_card())
        else:
            game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {user_hand}, score: {user_score}")
    print(f"Dealer's final hand: {computer_hand}, score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()
