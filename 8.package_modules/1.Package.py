"""
Python module is a single file , whereas a Python Package is a collection of modules .
Python package is a directory that contains Python modules and one additional file __init__.py
exemple : if we have a project to convert recording voice to mp3 Sound
direct : sound_conversion contain recToMp3.py

after a while another author add a file to convert voice to .wav format
direct: sound_conversion contain recToWav.py + recToMp3.py

after a while another author add a file convert voice to .wma
direct : sound_conversion contain recToWma.py + (recToMp3.py and recToWav.py)

In This Way , they make a Package just adding one more file __init__.py

let see an exemple
"""




