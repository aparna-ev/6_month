import  random
letters=['a','b','c','d','e','f','g','h','i','j','k','l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number=['1','2','3','4','5','6','7','8','9']
symbol=['!','#','$','%','^','&','*','@','&','(',')','*','+','_']
print("welcome to password generator")
no_letter=int(input("enter no of letters you wanna generate:"))
no_symbol=int(input("enter no of symbols you wanna generate:"))
no_number=int(input("enter no of numbers you wanna generate:"))
password=[]
for char in range(0,no_letter):
    password.append(random.choice(letters))
for char in range(0, no_symbol ):
    password.append(random.choice(symbol))
for char in range(0, no_number):
    password.append(random.choice(number))
#print(password)
random.shuffle(password)
#print(password)
final_password=""
for char in password:
    final_password+=char
print(final_password)
