
#functions in any programing lanuage can fall in two main categories .

# 1---> built-in functions
#built-in functions : they are predefined by programming lanuages and each serves a specific purpose .
#end you can get details about built-in functions in python documentation.


# 2---> User-defined functions
#user-defined functions : they are defined by users .


#Function with default argument
def info(name,age=40):
    print("my name is " + str(name) + " my age is : " + str(age))

info("ayadi mohammed",28)

#function variable length argument
#this function accept N  arguments

def function_with_unknow_number_of_argument(*args):
    print("number of args passed is : " + str(len(args)))
    for arg in args:
        print(arg)

function_with_unknow_number_of_argument(1,5,9,7,3,6)



#functions with key-value as variable length argument
#this function accept N pair key-value arguments

def function_with_keyValue_variable_length_argument(**keyValues):
    for key,value in keyValues.items():
        print("key : " + str(key) + " , value : " + str(value))

function_with_keyValue_variable_length_argument(name="ayadi",age=28,nationality="Morocco")

#we can declare a global variabl inside a function using keyword "global"
def simple_function(x):
    global var
    var= x

simple_function(10)
print(var)
print(
"""
#MEMORY MANAGEMENT

#in any language Memory is divided into two parts in any programing language .
#** Stack or run-time stack
#** Heap

#the Heap is a specific area of RAM where all values (objects) are stored . 
#the run-time stack never contain object ... it store only references pointing toward the values stored in the heap .




""")