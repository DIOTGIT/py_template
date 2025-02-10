import os
from os import walk
import shutil

start = os.getcwd() # 'c:\GPY'
exeptions = []
# exeptions = [
#             os.getcwd(),
#             r'c:\\'
#             ]       

v = []
w = walk(start)
for (dirpath, dirnames, filenames) in w:
    if '.venv' in dirnames and dirpath not in exeptions:
        v.append(dirpath + '\.venv'  )
    #print(dirpath, dirnames, filenames)

print(v)

for d in v:
    shutil.rmtree(d)