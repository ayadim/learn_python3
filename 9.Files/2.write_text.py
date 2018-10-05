

#Acces mode : this mode is used to append lines to file
write_file = open("writed_file.log","w")
for item in range(1,20):
    write_file.write("this is the item : " + str(item) + " \n")

list = ["this is a new \n" , "this is the second item \n","hhhhh\n"]
write_file.writelines(list)

write_file.close()


