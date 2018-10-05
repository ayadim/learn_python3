#we have the following list
list = ["abc",[2,3,("mohit","the avengers")],1,2,3]
#1 Get the string "avengers"

print(list[1][2][1].split(" ")[1])


#2 with the for loop , take the following list and sort it based on the sum of the values of the tuple of the list :

listOfTuple = [(1,5),(9,0),(12,3),(5,4),(13,6),(1,1)]
def getSum(x):
    return x[0]+x[1]

listOfTuple.sort(key=getSum)
print(listOfTuple)

#3 find the index of all 1
list3 = [1,2,4,5,1,1,4,1,56]
listOfIndex = []
for item in range(len(list3)):
    if list3[item] == 1:
        listOfIndex.append(item)
print(listOfIndex)






