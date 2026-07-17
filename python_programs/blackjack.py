import random
print("BLACKJACK GAME................")
def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    cards=random.choice(cards)
    return cards
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)# to change ace value from 11 to 1 according to the sum of cards
    return sum(cards)

def compare(u_score, c_score):
    if u_score==c_score:
        return "DRAW"
    elif c_score==0:
        return " Lose...the opponent has Blackjack"
    elif u_score>21:
        return "oops you lose ,went over 21"
    elif c_score>21:
        return "you win ,opponent went over 21"
    elif u_score>c_score:
        return "You win"
    else:
        return "You Lose"
def play():
    user_card=[]
    computer_card=[]
    computer_score=-1
    user_score=-1
    is_game_over=False

    for i in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    while not is_game_over:

        user_score=calculate_score(user_card)
        computer_score=calculate_score(computer_card)

        print(f"Your cards: {user_card}, current score: {user_score}")
        print(f"Computer cards: {computer_card[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            choice=input("would you like to chose another card 'y' or 'n' :").lower()
            if choice=="y":
                user_card.append(deal_card())
            else:
                is_game_over=True
    if user_score<=21:
        while computer_score !=0  and computer_score < 17:
            computer_card.append(deal_card())
            computer_score=calculate_score(computer_card)
    print(f"Your cards: {user_card}, final score: {user_score}")
    print(f"Computer cards: {computer_card},final score: {computer_score}")
    print(compare(user_score,computer_score))

while input("do you want to play again?(y/n) ").lower()=="y":
    play()
    print("\n"*20)
