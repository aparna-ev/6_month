import random
print("WELCOME TO HANGMAN GAME")
words=["camel","moon","butterfly","sunlight","python","job"]
chosen_word=random.choice(words)
#print(chosen_word)
placeholder=""
for char in chosen_word:
    print("-",end=" ")
stages = [
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
]
lives=6
game_over=False
correct=[]
while not game_over:
    guess=input("\nenter your guess:").lower()
    if guess in correct:
        print("already guessed")
    display=""
    for char in chosen_word:
       if char==guess:
            display+=char
            correct.append(char)
       elif char in correct:
           display += char
       else:
           display+="-"
    print(display)
    if guess not  in chosen_word:
        lives-=1
        print(f"**************{lives}/6 LIVES LEFT*************************")
        if lives==0:
            game_over=True
            print(f"***********you lose** the word is {chosen_word}***********")
    if "-" not in display:
        game_over=True
        print("you win")

    print(stages[lives])
    