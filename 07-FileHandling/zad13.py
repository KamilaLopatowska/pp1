movie_titles = ['clueless', 'mean girls', 'saw', 'love witch', 'barbie']

file = open('movies.txt', 'w')

for element in movie_titles:
    file.write(element +"\n")
file.close()