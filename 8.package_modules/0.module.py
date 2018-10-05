print("""
 A Python module is the Python source file .
 which consist of statement , Classes , Functions , Variables.
 
 """)

#Modules are code file meant to be used by other programs.
#in order to use a module , we use the import statement


from module2 import power #import only power() function from module2.py
import simpleModule as mymodule #import every thing in simpleModule.py
sum = mymodule.sum(10,2)
print(mymodule.name)
print(power(2,3))


#Locating module

import sys
print(sys.path)

#see all simpleModule module functions,variables and content
print(dir(mymodule))