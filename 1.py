list = []
from os import path
import string
def ReturnChar(path_file):
    for x in string.printable:
        list.append(x)
    for char in list:
        count = 0
        file = open(path_file,"r")
        for i in file:
           for c in i:
                if c == char:
                    count = count + 1
        if(count>0):
            if(char == '\n'):
                print("the character spacebar is found {} times in file".format(count))
            else:
                print("the character {} is found {} times in file".format(char,count))
ReturnChar("D:\liorn.txt")