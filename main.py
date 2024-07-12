import random

n = 0

n = random.randint(0,10)

if n == 4:
    print("You got the secret number")
else:
    print(f"Not the number. You chose {n}. Try again.")