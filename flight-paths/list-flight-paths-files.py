from os import listdir
from os.path import isfile, join

path = "downloaded-paths/"
files = [f for f in listdir(path) if isfile(join(path, f))]
print(files)
