list01 = [2,4,6,8,4,7,8,10,20,-1,4,-4]
sum = 0

# #1
for x in list01:
    print("#1 print x: ", x)

for x in range(2,10,1):
    print("#1b print x: ", x)

for x in range(1, len(list01),1):
    print("#1c print index #: ", x)
    print("#1d print value of index: ", list01[x])

# #2
for i in list01:
    sum += i
    print("#2 print i: ",i)
    print("#2 print sum: ",sum)

# #3
for i in list01:
    if i > 10:
        print("#3 i greater than 10: ", i)
    elif i == 10:
        print("#3 i is equal to 10: ", i)
    elif i < 1:
        print("#3 i less than 1: ", i)
    else:
        print("#3 other wise print i: ",i)

dict01 = {"favNum": 24, "NickName": "HoneyBee", "age": 42, "hobbies": ["Crocheting", "Gardening", "Minecraft"]}

# #4
for i in dict01:
    print("#4a print key:", i)
    print("#4b print value: ", dict01[i])

# #5
for i in dict01:
    if i == "favNum":
        print("favNum: ",dict01[i])
    elif i == "hobbies":
        print("hobbies: ", dict01[i])
    else:
        print("Sorry that was not found")