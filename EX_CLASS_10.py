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
#     worked- ex1 the long way
# print(d.items())
# ex 1
print([movies + 'is played by ' + actress for (movies, actress) in zip(movies, actress)])

# # ex2
# movie = dict(zip(movies, actress))
# print(movie)
# # worked- ex2 the long way
d = ({movies: actress for (movies, actress) in zip(movies, actress)})
print(d)

# ex3
# print(d.keys()+ 'is played by ' +d.values() for d)
print([movies + 'is played by ' + actress for (movies, actress) in d.items()])
# she codes way

# ex4
[print(i * 100) for i in range(1,10) if i%2==0]
# success by myself

# ex5
[print(x*100) if x%2==0 else print(x) for x in range(1,10)]
