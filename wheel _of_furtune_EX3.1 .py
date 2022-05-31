import random
def de_game():
    print('Welacome to the great game of all times')
    print("Notice you can only pick a number from 1- 10")
    x = None
    while range:
        n = random.randint(1, 10)
        x = input("   First things first, pick a number: ")
        x = int(x)
        if x == n:
            print('Congragelations, You Won')
            print("The numbers are equals")
            break
        else:
            print('Oh No!, You Lost')
            if x > n:
                print("The number you have chosen is greater")
            else:
                print("The number you have chosen is lower")
    return
de_game()
##completed## 10/4/21



def randomal(de_game):
    d = random.randint(1, 10)
    x = de_game()
    if x == d:
        print("yas queen")

randomal()

# # from random import randint
# # def de_game():
# #     print('Welacome to the great game of all times')
# #     print("Notice you can only pick a number from 1- 10")
# #     x = randint(1,10)
# #     ans = input("enter a number")
# #     ans.split(1, 10)
# #     if x == ans:
# #         print("you won")
# #     else:
# #         print("you're a loser")
# #
# # de_game()