import sys

#1 - Find the number of ways to find whether a key exists in a dictionary or not .
ports = {22:"ssh",23:"Telnet",53:"dns",80:"http",443:"https",50:"PO"}

print(sys.version)

print(ports)

given_key = 23
keys = ports.keys()
exist = given_key in keys

if exist :
    print("the key exist")
else:
    print("the key doesn't exist ")

print("----------- Method 2 to find if key exist or not ! --------------- ")
print(ports.__contains__(22))
revers_dict = {}
for key,value in ports.items():
    revers_dict[value] = key

print(revers_dict)

print(help(revers_dict))


