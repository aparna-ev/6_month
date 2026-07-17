import random
easy_level=10
hard_level=5
#checking the number-------
def check_answer(guess, hidden_number,turns):
    if guess<hidden_number:
        print("you guessed too low")
        return turns-1
    elif guess>hidden_number:
        print("you guessed too high")
        return turns - 1
    else:
        print(f"you guess is correct, the number is {hidden_number}")
        return turns


#choosing the difficulty-----
def set_difficulty():
    level=input("enter your difficulty level type 'easy' or  'hard' :").lower()
    if level=="easy":
        return easy_level
    else:
        return hard_level

print("Welcome to the Number Guessing Game..................")
def game():
    print("I'm thinking of a number between 1 and 100")
    hidden_number=random.randint(1,100)
    turns=set_difficulty()

    guess=0
    while guess!=hidden_number:
        guess=int(input("enter your guess: "))
        turns=check_answer(guess,hidden_number,turns)
        if guess==hidden_number:
            return
        print(f"You have {turns} attempts ramaining to guess the number")
        if turns==0:
            print(f"Oops , you lose the number is {hidden_number} ")
            return #to exit otherwise it will continue
        elif guess!=hidden_number:
            print("Guess again....")
game()