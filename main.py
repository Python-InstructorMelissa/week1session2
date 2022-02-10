# Know you need a function but don't know how you want it to go yet but still need to run your python file?
 
def nextFunction():
    pass

"""
Through out the next 2 months we are going to build ourselves a application.  Lets get our brainstorming started while working with functions

"""
movies = [
    {
        'id': 1,
        'title': "Back to the Future",
        'year': 1984,
        'actors': [
            {'name': "Michael J Fox"},
            {"name": "Christopher Lloyd"}
        ],
        'genre': "Syfy Drama"
    },
    {
        'id': 2,
        "title": 'Rambo 1st blood',
        'year': 1982,
        'actors': [
            {'name': "Sylvester Stallone"},
            {'name': "David Caruso"},
            {'name': 'Brian Denning'}
        ],
        'genre': 'Action'
    }
]
# Print the whole list
# print("whole list: ", movies)


# print Back to the Future only
# print("just back to the future: ", movies[0])

# print just the movie titles for the whole list
# for movieName in movies:
#     print("all movie titles in list: ", movieName['title'])

# print(movies['title'])  #This will error out
# print(movies[0:1]['title']) # This also errors out

greatMovie = movies[0]['actors']
# print(greatMovie)
anotherMovie = movies[1]['actors']

def actors(var):
    for a in var:
        print("all the actors: ", a['name'])

# actors(greatMovie)
# actors(anotherMovie)

# aList = []
# print("before function:", aList)
def actorList(var):
    aList = []
    print("before function:", aList)
    for a in var:
        aList.append(a['name'])
    print("the list of actors inside function: ", aList)

# actorList(greatMovie)
# actorList(anotherMovie)
# print("after function", aList)

for movie in movies:
    if movie['title'] == "Back to the Future":
        print("Yay you found my favorite Movie")
    elif movie['title'] == "Rambo":
        print("this one is ok")
    else:
        print("sorry ran out of movies")