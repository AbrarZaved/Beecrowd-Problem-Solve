import random
num = int (input("Enter your guess between 1-10: "))
number1 = random.randint(1,10)
if num==number1:
    print("Your Guess is right")
else:
    print("You are wrong")
    print("Random Number was: ",number1)