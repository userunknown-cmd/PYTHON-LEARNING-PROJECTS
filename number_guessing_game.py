import random

computer = random.randint(1,5)
you = int(input("Enter the number from 1 to 5:"))

if(you==computer):
    print("you guessed it right")
else:
    print("lets guess again!!!")    
    print(f"computer choose {computer}")