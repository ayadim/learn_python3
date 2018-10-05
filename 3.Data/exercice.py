

#chapter 3
#Exercice


#1 Obtain the (thapar.edu) name from this url : http://www.thapar.edu/index.php/about-us/mission.
#2 You have the tuple tup = ('www','thapar','edu','index','php','about-us','mission') . now make the full link www.tapar.edu/index.php/about-us/mission



#1 get the (tapar.edu)
url = "http://www.thapar.edu/index.php/about-us/mission"

#solutions of the first question
print(url.split("www.")[1].split("/")[0])
#OR
print(url.split("/")[2].split("www.")[1])
#Or
print(url[(url.find(".")+1):(url.find("/",url.find("."),len(url)-1))])

#2 tup = ('www','thapar','edu','index','php','about-us','mission')  make www.tapar.edu/index.php/about-us/mission
tup = ('www','thapar','edu','index','php','about-us','mission')
chars=[".",".","/",".","/","/"]
url = ""
for item in range(len(chars)):
    url += tup[item] + chars[item]
url+=tup[len(tup)-1]
print(url)