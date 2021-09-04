import hashlib
import os
class File:
    def __init__(self, path):
        self.path = path
    def Md5(self,path):
        with open(self.path, 'rb') as fh:
            m = hashlib.md5()
            while True:
                data = fh.read(8192)
                if not data:
                    break
                m.update(data)
            return m.hexdigest()
    def NameFile(self,path):
        basename = os.path.basename(self.path)
        return basename