# Know you need a function but don't know how you want it to go yet but still need to run your python file?
 
def nextFunction():
    pass

"""
Through out the next 2 months we are going to build ourselves a Park Organization.  Lets get our brainstorming started while working with functions

"""
parks = [ # parks = list of dictionaries
    {
        'zooName': 'NinjaZoo',
        'animals': [ # animals is the key the value is a list of dictionaries
            {'species': 'Lion', 'count': 2, 'names': [
                {'name': 'Simba'},
                {'name': 'Nala'}
            ]},
            {'species': 'Tiger', 'count': 3, 'names': [
                {'name': 'Tigger'},
                {'name': 'Tango'},
                {'name': 'Mara'}
            ]},
            {'species': 'Bear', 'count': 1, 'names': [
                {'name': 'Smokey'}
            ]}
        ]
    },
    {
        'zooName': 'HoneyBeeZoo',
        'animals': [
            {'species': 'Lion', 'count': 4, 'names': [
                {'name': 'DewDrop'},
                {'name': 'Scar'},
                {'name': 'Fred'},
                {'name': 'Margaret'}
            ]},
            {'species': 'Tiger', 'count': 1, 'names': [
                {'name': 'Janice'}
            ]},
            {'species': 'Bear', 'count': 2, 'names': [
                {'name': 'Yogi'},
                {'name': 'Booboo'}
            ]}
        ]
    }
]
# print(parks)
# print(parks[0])
zoo = parks[0]
# print("Print 1st zoo: ", zoo)
# print("Zoo Name: ", zoo['zooName'])

def printParks(a):
    for p in a:
        print("A Park: ", p)

# printParks(parks)

def printParkNames():
    print(parks[0]['zooName'])
    print(parks[1]['zooName'])

# printParkNames()

def printParkNames2(a):
    for p in a:
        print(p['zooName'])

# printParkNames2(parks)

def printParkAnimals(a):
    for p in a:
        print("The park Animals: ",p['animals'])

# printParkAnimals(parks)

def returnZooName(a):
    for z in a:
        return z['zooName']

zooNames = returnZooName(parks)
# print("Zoo Names: ", zooNames)

def conditionalOne(a, b, s, c): # function requiring 4 arguments
    for z in a: # loop through the data set of what ever a is
        if z['zooName'] == b: # if z is = the value of arg b then...
            print("The Zoo's Name: ", z['zooName']) # print the value then....
            for animals in z['animals']: # loop through the animal values then ....
                if animals['species'] == s: # if the species is = the values of arg s then...
                    print("The Species: ", animals['species']) # print the value then ...
                    species = animals['species']  # set species to that value then....
                    print("How many do we have? ", animals['count']) # print the # of those species then...
                    count = animals['count'] # set count to the # of those animals then....
                    for n in animals['names']: # loop through their names then ...
                        if n['name'] == c: # if the name is = the value of arg c then....
                            print("My name is: ", n['name']) # print the name then...
                            myName = n['name'] # set myName to that value
                        else: # if the name doesn't match ...
                            print("Name Fail")
                else: # if the species doesn't match ...
                    print("Species Fail")
            return f"The Zoo's Name is {z['zooName']}, we have {count} {species}(s), one of the name's is {myName}." # if all is true return the following
        elif z['zooName'] == b:
            return "The other Zoo: ", z['zooName']
        else: # if the zoo name doesn't match ...
            print("You spelled something wrong dummy")
# conditionalOne(parks, "NinjaZoo", "Lion", "Nala")

theResult = conditionalOne(parks, "HoneyBeZoo", "Lion", "Simba")
print("Final Result: ", theResult)