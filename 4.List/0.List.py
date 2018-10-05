# like tuple , a list is also buit-in data struct available in python .
#list may contain items of different types .
from builtins import list

list = ["ayadi mohammed",28,"morocco"]
for item in list :
        print(str(item) + " "+ str(type(item)))


#Unpacking list values
name,age,country = list
print("my name is : "+name)

#concatenated two list
list = list + [2018,98,12.5]
print(list[:]) #['ayadi mohammed', 'age', 28, 'morocco', 2018, 98, 12.5]



#update list
list[0] = "ayadi"

#Delete value from list

    #delete by value using remove() method
list.remove(2018)
print(list)


    #delete byb value using the key word DEL
del list[-1]
print(list)

#append item to list
list.append("appended")
print(list)
        #OR
list = list + [5]
print(list)

#extend (append list2 to list1 )
l1 = ["c","a","b","d"]
l2 =["E","F","I","J"]

l1.extend(l2) #add all element of l2 to l1
print(l1)

print("--------------------------------------")

#splite
print(list[0])# print first item in list
print(list[-1]) # print last one in list
print(list[:2]) # print items starting from beginning to the index 2 (exclude index 2 )

# multiplication of list
list = list*2
print(list[:]) #['ayadi mohammed', 'age', 28, 'morocco', 2018, 98, 12.5, 'ayadi mohammed', 'age', 28, 'morocco', 2018, 98, 12.5]



#count() method is used to find the occurence of an item in a list .
print("Count the oucurence of  'ayadi' in list  : "+str(list.count("ayadi")))


#Index() method used to find the index of particular item in list .
print("The index of item 'morocco' is : " + str(list.index("morocco")))

#insert() method insert  value in list using given index

print(list)
list.insert(list.index("morocco"),"maroc")
print(list)

#pop(index) remove and return  item using index . pop() remove and return the last item in list
print(" ------------------------ Poping ------------------ ")
print(list.pop())
list.pop(list.index("maroc"))
print(list)


#reverse list
print(list)
list.reverse()
#OR
#list.sort(reverse=True)

print(list)

print(list+[1555555,55555555])







# --------------------   BUILT IN FUNCTIONS

# list(tupel) convert tupel to list (tuple or string )
# t = ("b","a","c")
# l = list(t)
# print(l)
# #clear list
# list.clear()

#sort a list
# list.sort(cmp=None , key=None , reverse = False)
l1= ["c","a","b","d"]
l1 = sorted(l1)
#OR
#list.sort()
print(l1)

#Reverse list item
#list.sort(reverse=True)


#Sort list of tupls  according to second value in tuple
list_tup = [("b",2),("c",3),("a",1),("d",4)]

def getKey(x):
        return x[1]

list_tup.sort(key=getKey)
print(list_tup)


#List comprehension to creat new list using For loop
list = [2,4,6,8,5,4,1]
list2 = [(item*2) for item in list]
print(list2)



