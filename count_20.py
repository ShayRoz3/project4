def count():

    num = 0
    while num < 20:
        num += 1
        print(num)
        guess1 = int(input("pick your number:"))
        if num == guess1 and num % 7 != 0:
            print(num)
        elif num == guess1 and num % 7 == 0:
            print("boom")
        else:
            break

count()
