import random

from art import logo

def deal_card():
    # return a random card from the deck
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and returns sum of all cards in the list as the score"""
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#to compare the scores
def compare(u_score, c_score):
    if u_score==c_score:
        return "draw 🙃"
    elif c_score==0:
        return "Lose!, Opponent has Blackjack! 😱"
    elif u_score==0:
        return "Win!, with a Blackjack! 😎"
    elif u_score>21:
        return "You went over, You lose! 😢 "
    elif c_score>21:
        return "Opponent went over, you win! 😅"
    elif u_score>c_score:
        return "You win! 🙂"
    else:
        return "You lose! 🤕"


def play_game():

    print(logo)
    user_cards=[]
    computer_cards=[]
    computer_score=-1
    user_score=-1
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards : {user_cards} and score is {user_score} ")
        print(f"Computer's first card  : {computer_cards[0]} ")

        if user_score==0 or computer_score==0 and user_score>21:
            is_game_over=True
        else:
            user_deal=input("Type 'y' to deal another card, Type 'n' to pass :  ").lower()
            if user_deal=="y":
                user_cards.append(deal_card())
            else :
                is_game_over=True

    #for the dealer to follow their strategy
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} , final score : {user_score}")
    print(f"Computer's final hand : {computer_cards} , final score : {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? , Type 'y' for yes and 'n' for no ").lower()=="y":
    print("\n"*20)
    play_game()
