# ex_1: used google
def is_anagram(s,t):
    if sorted(s) == sorted(t):
        print(True,"- this is an angram")
    else:
        print(False, "- this is not an angram")

is_anagram("listen", "silent")
is_anagram("car", "cat")

num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
           (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
def num2roman(num):

    roman = ''

    while num > 0:
        for i, r in num_map:
            while num >= i:
                roman += r
                num -= i

    print(roman)
num2roman(1184)
# google way- want to do it on my own