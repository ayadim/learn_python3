import codecs
file = open("/root/Desktop/data","r")
readFile = file.read()
str=""
for item in readFile:
    if (item !=" " and item !="\n") :
       str+=item
print(codecs.decode("10181A325528130F010D24","hex"))
