import os.path
import os
import hashlib
def VirtualDisk():
    dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
    return(drives)
def Md5(filePath):
    try:
        fh = open(filePath, 'rb') 
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()
    except IOError:
        return None
        
def NameFlle(path):
    basename = os.path.basename(path)
    return basename
disks = VirtualDisk()
names = []
content = []
# Importing the os library

for disk in disks:
    # The path for listing items
    path = disk+'/'
    
    # List of files in complete directory
    file_list = []

    for path, folders, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(path, file))
    # Loop to print each filename separately
    for filename in file_list:
        name = NameFlle(filename)
        #print(names)
        if(os.access(filename, os.R_OK)):
            md5_file = Md5(filename)

        #print(md5_file)
        #print(md5_file)
        if(md5_file == None):
            break
        if(name in names and md5_file in content):
            print("the file {} is duplicate with same name and same content".format(name))
        elif name not in names:
            #print("elif 1")
            names.append(name)
        elif name in names:
            #print("elif 2")
            print("the file {} is duplicate with names".format(name))
        if md5_file not in content:
            #print("elif 3")
            content.append(md5_file)
        elif md5_file in content:
            #print("elif 4")
            print("the file {} is duplicate with content".format(name))
