class Movie:
    def __init__(self, title, hero, heroine):
        self.title=title
        self.hero=hero
        self.heroine=heroine

    def info(self):
        print('movie name: ', self.title)
        print('Hero name: ', self.hero)
        print('Heroine name: ', self.heroine)

list_of_movies=[]
while True:
    title=input('enter movie name: ')
    hero=input('enter hero name: ')
    heroine=input('enter heroine name: ')
    m=Movie(title, hero, heroine)
    list_of_movies.append(m)
    print('Movie added to the list successfully')
    option=input('Do you want to add another movie? [Yes|No]: ')
    if option.lower() == 'no':
        break

print('All Movies Information...')
print('#'*40)

for movie in list_of_movies:
    print("........")
    movie.info()
