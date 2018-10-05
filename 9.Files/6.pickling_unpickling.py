import pickle

# NAME
#     pickle - Create portable serialized representations of Python objects.
#
#     discription : the pickle module is used to store complex data such as list and dictionaty.
#
#
#
#
#     Classes:
#
#         Pickler
#         Unpickler
#
#     Functions:
#
#         dump(object, file)
#         dumps(object) -> string
#         load(file) -> object
#         loads(string) -> object
#
#     class Pickler(builtins.object)
#      |  This takes a binary file for writing a pickle data stream.
#
#
#     class Unpickler(builtins.object)
#      |  This takes a binary file for reading a pickle data stream.
#
#


#Pickling
from operator import length_hint

name = {"ayadi","mohamed","brahim","smail"} #SET collection that order item alphabitic
skils = ["Python","Php","C","C++","Java"]

pickle_on = open("employe.data","wb")
pickle.dump(skils,pickle_on)#Note the usage of “wb” instead of “w” as all the operations are done using bytes.
pickle.dump(name,pickle_on)
pickle_on.close()


#Unpickling
pickle_off = open("employe.data","rb")

for item in pickle_off.readlines():
    print()
    print("------")

# object = pickle.load(pickle_off)
# object = pickle.load(pickle_off)
# print(object)
# print(object_)
pickle_off.close()


