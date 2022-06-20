movies = ['The Notebook', 'Maleficent', 'Batman vs Superman', 'Black Swan',
          'Gone Girl', 'War of The Worlds', 'Just Married']
# print(movies)
actress = ['Rachel McAdams', 'Angelina Jolie', 'Gal Gadot',
           'Natalie Portman', 'Rosamund Pike', 'Dakota Fanning', 'Brittany Murphy']
# print(actress)

# ex1
# d = dict(zip(movies, actress))
# print(d)
# for key in d:
# print(key, 'is played by', d[key])
#    worked- ex1 the long way
# print(d.items())
# ex 1
print([movies + 'is played by ' + actress for (movies, actress) in zip(movies, actress)])
# tha lambada way
print(list(map(lambda x, y: x + 'is played by ' + y, movies, actress)))

# # ex2
# movie = dict(zip(movies, actress))
# print(movie)
# # worked- ex2 the long way
d = ({movies: actress for (movies, actress) in zip(movies, actress)})
print(d)
print(list(map(lambda x, y: x + ': ' + y, movies, actress)))
# i think that's what they ment- lambada way

# ex3
# print(d.keys()+ 'is played by ' +d.values() for d)
print([movies + ' is played by ' + actress for (movies, actress) in d.items()])
# she codes way

# ex4
[print(i * 100) for i in range(1, 10) if i % 2 == 0]
# success by myself
print(list(map(lambda x: x * 100 if x % 2 == 0 else "-", range(1, 10))))

# ex5
# [print(x*100) if x%2==0 else print(x) for x in range(1,10)]
# easy breasy
print(list(map(lambda x: x * 100 if x % 2 == 0 else x, range(1, 10))))

# ex 6
[print(x) if x % 7 != 0 else print("boom") for x in range(1, 99)]
print("-")
print(list(map(lambda x: "boom" if x % 7 == 0 else x, range(1, 15))))

# ex 7
sum = lambda x, y: x + y
print(sum(10, 1))
# she codes

# ex8
print([(x, y) for x in range(1, 7) for y in range(1, 9)])
# she-codes

# ex9
jouls = [5000, 8000, 10000, 6000, 12000]
[print(list(map(lambda x: (x, x / 4184), jouls)))]
# done

# ex 10
languages = ["HTML", "JavaScript", "Python", "Ruby"]
[print(list(filter(lambda x: x == "Python", languages)))]
# half half me
