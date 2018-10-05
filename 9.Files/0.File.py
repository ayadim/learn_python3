# you will use open() built-in function to open file . (the function create an file_object  object )
#file_object = open(file_name,acces_mode) acces mode is READ,WRITE,APPEND,...

file  = open("/root/Desktop/wifi","r")

# Read() method

#print(file.read()) Read all file
print(file.read(200)) #Read first 10 chars
print(file.read(30)) #Read next 10 chars
print(file.read(15)) #Read next 10 chars
file.close()

