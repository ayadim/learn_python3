#IF ... elif...else


#loops
#Range()

# class range(object)
#  |  range(stop) -> range object
#  |  range(start, stop[, step]) -> range object
#  |
#  |  Return an object that produces a sequence of integers from start (inclusive)
#  |  to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
#  |  start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
#  |  These are exactly the valid indices for a list of 4 elements.
#  |  When step is given, it specifies the increment (or decrement).
# print(help(range(10)))
from pip._vendor.msgpack.fallback import xrange

for item in range(0,10,2):
    print(item)


#result 0 2 4 6 8


#the xrange() is quit similar to range() except that xrange() releases or frees the memory when not in use .
#whereas range() doesn't release the memory .
x= 0
for item in xrange(20):
        print("hello world !")


for char in "this is a sentence !!! ":
    print(char)


list = [char for char in "this is a sentence ! "]
print(list)

#indefinite Loop

#try to get from user a valid integer
#
test = True
while test :
    test = False
    try:
        input = int(input("please enter a valid integer (-1 to exit) : "))
    except:
        print("invalid integer !")
        test = True

if input == -1:
    exit()
if test == False:
    print("valid number " )

#pass : do nothing but if we want to create a function for futur use we can't leave it emty . using pass avoid empty case

def muFun(x):
    pass
