import random
print("welcome to the game")
print("what u choose rock-0,paper-1,scissors-2")
choice=["rock","paper","scissors"]
player=int(input("enter rock,paper,scissors:"))
if player < 0 or player > 2:
    print("Invalid choice!")
else:
     print("your choice",choice[player])
     computer=random.randint(0,2)
     print("computer chose ",choice[computer])
     if player==computer:
         print("It's a tie")
     elif player==0 and computer==2:
        print("You win")
     elif player==2 and computer==0:
         print("You lose")
     elif computer>player:
        print("you lose")
     else:
        print("you win")