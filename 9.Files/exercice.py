#we need to count how many time a given word is in the text.txt file
#we should respect case sensitive

read_file = open("text.txt","r")
read = read_file.readlines()
read_file.close()
input = input("Please enter a word : ")
count = 0
for line in read:
    if input.lower() in line.lower():
        count +=1
print("number of ouccurance is : " + str(count))
