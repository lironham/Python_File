import os
from pathlib import Path

def process(p):
    #return if the path exist and if not create all parents folder
    if not os.path.exists(p):
        path = Path(p)
        path.mkdir(parents=True)
    p = p+"/process.txt"
    output = os.popen('wmic process get description, processid').read()
    fp = open(p, 'w')
    fp.write(output)
    fp.close()
#call to Function with r in begining
process(r'D:\temp\x')