#calling package in another path its possible using 2 lines
import sys
sys.path.append("./chapter8/")
# we added the new path for python to look for our package


from sound_conversion import recToMp3
from sound_conversion.recToWav import rec2Wav #import rec2Wav() function in recToWav.py module
#let's call package sound_conversion
print(recToMp3.rec2Mp3())
print(rec2Wav())
#get error NameError: name 'recToMp3' is not defined




