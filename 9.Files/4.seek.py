#the seek method return the pointer to the index 0
"""
 |  seek(self, cookie, whence=0, /)
 |      Change stream position.
 |
 |      Change the stream position to the given byte offset. The offset is
 |      interpreted relative to the position indicated by whence.  Values
 |      for whence are:
 |
 |      * 0 -- start of stream (the default); offset should be zero or positive
 |      * 1 -- current stream position; offset may be negative
 |      * 2 -- end of stream; offset is usually negative
 |
 |      Return the new absolute position.
 |


"""


file = open('text.txt','r')
content = file.read()

print(content)

print("----------------------- \n " + str(type(content)) + "\n -------------------")

print("----------------- read file again ")
#<problem>
content = file.read()
print(content)
#</prblem >
print("nothing readed because the pointer is in the end of file EOF ")
print("-----------------------  solution --------------- ")
file.seek(0)
content = file.read()
print(content)

print(help(file))



file.close()