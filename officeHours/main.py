myList = [1,2,3,4,5,6,7,8,9]
result = 0


#  #1
# for i in myList:
#     print("#1 Printing myList: ", i)

# #  #2
# for i in range(len(myList)):
#     print("#2 Printing myList: ", myList[i])

#  #3
# print("#3 print the 5: ", myList[4])

#  #4
theResult = sum(myList)
# print("#4 Print result: ", theResult)

# #5
for i in myList:
    result += i
# print("#5 Print result: ", result)

# #6
# for i in myList:
#     if i < 2:
#         print('#6a I is less than 0: ', i)
#     elif i < 5:
#         print('#6b i is less than 5: ', i)
#     elif i == 5:
#         print('#6c i is equal to 5: ', i)
#     else:
#         print('#6d other wise print: ', i)

melissa = {"favoriteNumber": 24, "meaning": "HoneyBee", "age": 43, "hobbies": ["Crocheting", "Garding", "Playing Minecraft"]}

# #7
# for m in melissa:
#     print("#7a print key of m: ", m)
#     print("#7b print value of m: ", melissa[m])

# #8
print("#8a", f"Melissa's favorite number is {melissa['favoriteNumber']}")
print("#8b print melissa's favorite number: ", melissa['favoriteNumber'])
