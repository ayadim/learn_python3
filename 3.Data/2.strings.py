

#beside numbers, python can also manipulate strings
#strings can be enclosed in single quotes ('....')
#Or can be enclosed between double quotes("...")
from builtins import print, list

print(" She say : \" hi every one \" .")
line = "first line. \nSecond line. \nthird line. \n"

print(line)

#if you don't want charachters prefaced by \ to be interpreted as special chars . use raw (r) before quotes / double quotes

    #problem
print("c:\Some\name")

        #output \n mean new line
        #c:\Some
        #ame

    #solution
print(r"c:\Some\name") #IndentationError: unexpected indent

        #output
        #c:\Some\name

#String can span multi lines using tripple quotes  """ .... """     OR    ''' ..... '''

menu =""""\
This is my Menu : 
    [first option : ] [:] [...............]
   [second option : ] [:] [...............]
"""

    #Output
print(menu)

# strings can be concatenated using + operator . and repeated using *
name = "ayadi"
print("Hi" + " my" + " name is " + name)
print("printing char A 20 times start ... \n" + ("A" * 20))
print(5*"Ha" + "!")

#---> two or more strings letirals (no variable or experience  )are next each other automatically are concatenated .
name = "aya" "di" " " "moham" "med" #well concatenated
#name  = "aya" "di"  + nameVariable
text = ("this is a l" + 8*"o"+"ng "
        "string ........... concatenated ! ")
print(text)

#Strings can be indexed and we can call each char using index that start from 0 to (string.__len__() - 1)
#name = "ayadi mohammed"
    #call the first char in string
print(name[0])
    #call the three first chars in string
print(name[:3])
    #call the three last chars in name string
print(name[-3:])
    #call the last char in string
print(name[name.__len__()-1]) #name length
#OR
print(name[-1])

    # $[:i] + $[i:] always equals to $ variable value
print(name[:3] + name[3:])

#slice indices
print(name[:3]) # start from the beginning  to the 3 third  char (char with 3 indice  is excluded !) .
print(name[3:]) # start from the 3 indice to the end (char with 3 indice is included ! )

print(name[(-1)*name.__len__()]) # first char (-length) indice or indice 0.
print("the length of name variable is " + str( len(name))) # str() : to cast int value to string value . len() get the length of string
#------------------------ strings Functions
print("\n #------------------------ strings Functions ------------------#\n ")
string = "write any thing in your mind"
print(string)
#the count(substr,[start],[end]) method retourn the number of occurences of the substring given .
print("count the character 'n' in the sentence : " + str(string.count('n')))
#OR
print(string.count('i',3,20))



#finding the index of substring 'any' starting from index 0 to 20
print(string.find("any",0,20))

#or finding the index of substring 'in' in the string starting from left
print("'in' position starting from left is : " + str(string.find("in")))

#find a substring starting from right
print("'in' position starting from right is : " + str(string.rfind("in")))

#------------------String Case methods
print("\n#------------------ String Case methods --------------------# \n")
stringTitled = "This Is a Sentence ! "
print(string.upper())#to upper . (this is an exemple --> THIS IS AN EXEMPLE )
print(string.capitalize()) # capitalise the first character in line . ( this is an exemple --> This is an exemple )
print(string.title()) #convert every first character in line . ( this is an exemple --> This Is An Exemple )
print(stringTitled.swapcase()) #swap all cases  . (This An ExeMple --> tHIS aN eXEmPLE )
print("ayadi".isalpha()) # is alphabetic
print("111".isalnum()) # is number

#------------------ String Strips
# Some times we encounter the problem of undesirable space or char at the beginning or end string

stringToStrip ="       This a string that containt undiserable ! character at the beginning end !!!!!"
print(stringToStrip.lstrip(" ")) # remove all th spaces in string beginning
print(stringToStrip.rstrip("!")) # remove all ! chars in the end of string
print(stringToStrip.lstrip(" ").rstrip("!")) # call lstrip() and rstrip() to remove the beginning and end of string
print(stringToStrip.strip()) # remove from both sides . by default the character given is space you can change it (strip('!'))



# ------------- String Split methods -------------
print("\n# ------------- String Split methods -------------\n")
#some time we need to split a piece string to get a part of string . for exemple if we want to get year from this str '30-05-1998'
anyDate = "30-05-1998"
listOfPieces = anyDate.split("-")
print(listOfPieces)
for item in (listOfPieces):
        if len(item) > 2 :
                print("year is : " + str(item))

#------------------ Buid-in Funcftions And String
#let's see how build in function deal with string argument min() max()

#Consider you need to find the minimum character from a given string according to the ASCII value
stringX = "ABCD"
print(min(stringX))
print(max("ABCD")) #According to ASCCI value 'D' is the max value from list of CHARS... .
#in many situation we need to convert float or int to sting valule we call build-in function to cast
stringValue = str(1115.2) #cast float value to string
print(stringValue)

thisIsFloatValue = float(stringValue)
print(thisIsFloatValue)
print(type(stringValue)) # get type of stringValue variable
print(type(thisIsFloatValue)) # get the type of variable / or get the class of vriable



#using IN operator to find substring in String Given
        #IN operator is used with If statement

if "age" in "this is my age " :
        print("exist !")
else:
        print("not exist !")




