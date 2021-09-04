import os.path
import os
import hashlib
from file import File
from collections import Counter
def VirtualDisk():
    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    return(drives)
disks  = VirtualDisk()
names = []
content = []
both = []
name_md5 = {}
for disk in disks:  
    # The path for listing items
    path = disk+"/"
    
    # List of files in D directory
    file_list = []

    for path, folders, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(path, file))
    # Loop to print each filename separately
    for file1 in file_list:
        filename = File(file1)
        name = filename.NameFile(filename)
        #print(names)
        if(os.access(file1, os.R_OK)):
            md5_file = filename.Md5(filename)
            name_md5[md5_file] = name
        if(name in names and md5_file in content):
            both.append(name)
        
        names.append(name)
        content.append(md5_file)
    names_dict = Counter(names)
    content_dict = Counter(content)
    both_dict = Counter(both)
    print(name_md5)
    for x in names_dict:
        if names_dict[x]>1:
            print("the file {} is duplicate with name {} times".format(x,names_dict[x]))
    for x in content_dict:
        if content_dict[x]>1:
            name = name_md5.get(x)
            print("the file {} is duplicate with content {} times".format(name,content_dict[x]))
    for x in both_dict:
        if both_dict[x]>1:
            print("the file {} is duplicate with same name and same content {} times".format(x,both_dict[x]))
    