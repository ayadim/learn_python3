

#Data structure

#Tuple can hold different data type as Integer , Float , String etc

#create empty tuple

myTuple = ()
mySecondTuple = ()
print(type(myTuple)) #<class 'tuple'>
myTuple = ("Exemple",12,12.5,'!',mySecondTuple)
for item in myTuple:
    print(str(item) + "  : type -->  " + str(type(item)) )

myThirdTuple = 1,2,3,'a'
for item in myThirdTuple:
    print(str(item))

print("first element : " + str(myThirdTuple[0]))
print("last  element : " + str(myThirdTuple[-1]))

#Slice Tuple
print(myTuple[1:3])


#Upacking the items of tuple

a,b,c,d = myThirdTuple

# Operation against tuple
tuple1 = ("value1","value2")
tuple2 = ("value3","value4","value5")
tuple3 = tuple1 + tuple2
print(tuple3)#('value1', 'value2', 'value3', 'value4', 'value5')

tuple4 = tuple1 * 3  #('value1', 'value2', 'value1', 'value2', 'value1', 'value2')
print(tuple4)