import random

guess = str(input("rock paper scissors?"))
lisyt = ["rock", "paper", "scissors"]
# need to generate random number
if guess == "paper":
    if random.choice(lisyt) == lisyt[0]:
        print("paper cover rock, you won")
    elif random.choice(lisyt) == lisyt[2]:
        print("you have lost, scissors won")
    else:
        print("tie")
elif guess == "rock":
        if random.choice(lisyt) == lisyt[2]:
            print("rock break scissors, you won")
        elif random.choice(lisyt) == lisyt[1]:
            print("you have lost, paper won")
        else:
            print("tie")
elif guess == "scissors":
    if random.choice(lisyt) == lisyt[1]:
        print("scissors cut paper, you won")
    elif random.choice(lisyt) == lisyt[0]:
        print("you have lost, rock won")
    else:
        print("tie")






# this game generate a random numer and check if my answer matched the computer
# and it works