
#ReadLine() Method

# in order to read line by line use readLine()
print("---------- readLine() Method ------------ ")
file_input = open("/root/Desktop/wifi","r")

print("----------- #read first line -------------- ")
print(file_input.readline())
print("----------- #read second line -------------- ")
print(file_input.readline()) #read second line
print("----------- #read third line -------------- ")
print(file_input.readline()) # read third line
print("----------- #read the 20 chars of the 4th line -------------- ")
print(file_input.readline(10)) # read the 20 chars of the 4th line

print("----------- #read the rest of file  --------------\n ")

# read each line in file
# file_input.readlines() -> return List[] of items (lines)
for line in file_input.readlines():
    print(line)

file_input.close()



