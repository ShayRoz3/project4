# ex_1: used google
def is_anagram(s, t):
    if sorted(s) == sorted(t):
        print(True, "- this is an angram")
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

num2roman(1917)
# google way- want to do it on my own

# ex3
def num_plus1(n):
    if n [ -1 ] < 9 :
        n [ -1 ] += 1
    elif n [ -1 ] >= 9 :
        n [ -1 ] = 0
        n [ -2 ] += 1
        if n [ -2 ] >= 9 :
            n [ -2 ] = 0
            n [ -3 ] += 1
            if n [ -3 ] >= 9 :
                n [ -3 ] = 0
                n [ -4 ] += 1
    return n
print(num_plus1([1,9,9,9]))

#
# def is_work(k):
#     for i in k:
#         print(i, end= "")
# is_work([1,2,3,9])
#nice oprion- turn to int but dodn't worked out

l = [1, 9, 9]
l = [1,2,3,4]
l = [1,2,3,4,5,6,7,8,9]
s = [str(integer) for integer in l]
a_string = "".join(s)
res = int(a_string)
print(res)
new = res + 1
print(new)

r2 = [int(y) for y in str(new)]
print(r2)