# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def whiley():

    second = 0
    while second < 20:
        second += 1
        pick = int(input("next number is? "))
        if pick == second and pick % 7 != 0:
            print(second)
        elif (pick == second) and (pick % 7) == 0:
            print("boom")
        else:
            print("this is a mistake")
            break

whiley()