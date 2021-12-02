# Know you need a function but don't know how you want it to go yet but still need to run your python file?
 
def nextFunction():
    pass

"""
Through out the next 2 months we are going to build ourselves a application.  Lets get our brainstorming started while working with functions.
Just adding a comment

"""
inventory = [
    {
        'listOwner': 'Melissa',
        'listItems': [
            {'location': 'Living Room', 'count': 1, 'items': [
                {'item': 'couch'}
            ]},
            {'location': 'Living Room', 'count': 2, 'items': [
                {'item': 'Left End Table'},
                {'item': 'Right End Table'}
            ]},
            {'location': 'Living Room', 'count': 1, 'items': [
                {'item': 'TV'}
            ]}
        ]
    },
    {
        'listOwner': 'Mel',
        'listItems': [
            {'location': 'Kitchen', 'count': 1, 'items': [
                {'item': 'table'}
            ]},
            {'location': 'Kitchen', 'count': 4, 'items': [
                {'item': 'chair01'},
                {'item': 'chair02'},
                {'item': 'chair03'},
                {'item': 'chair04'}
            ]},
        ]
    }
]
# print(inventory)
# print(inventory[0])
melissa = inventory[0]
mel = inventory[1]
# print("Melissa's list: ", melissa)
# print("Mel's list: ", mel)
# print("List owner: ", melissa['listOwner'])
# print("List owner: ", mel['listOwner'])

def printOwner(user):
    print(f"{user['listOwner']}'s List")

# printOwner(melissa)
# printOwner(mel)

def printItems(user):
    # print(f"{user['listItems']}")
    for i in user['listItems']: # go through the listItems and pull out each index
        for o in i['items']: 
            print(f"{o['item']}")

# printItems(mel)

def wrong():
    print("Sorry not a match")


def ifOne(user, owner):
    if user['listOwner'] == owner:
        print(printItems(user))
    else:
        print(wrong())

# ifOne(melissa, 'melissa')
# ifOne(melissa, 'Melissa')
# ifOne(mel, "Melissa")
# ifOne(mel, "Mel")

#15
def foo():
    print(1) # print number 1
    x = bar() # x = function bar()
    print(x) # executing the function of bar()
    return 10 # returning 10

def bar():
    print(3) # print the number 3
    return 5 # return 5

y = foo() # setting y = the foo() function
print(y) # executing the function foo()

