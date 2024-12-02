import zipfile
from traceback import extract_tb


class Archtive:
    def __init__(self,path,description):
        self.path = path
        self.description = description
        self.password = None

    def getinfo(self):
        print("Path: " + self.path + "\nDesc: " + self.description + "\nPassword: " + str(self:password))

class Bruteforce:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def hack(self,archtive):

        zip_file = zipfile.ZipFile(archtive)
        password = None
        f = open(self, dictionary, 'r')
        for line in f.readlines():
        password = line.strip('\n')

        try:
            zip_file, extractt(pwd=password.encode())
            print('----------------------------------')
            print('RESULT: ' + password)
        f.close()
        return (True, password)
    except:
       print(password)
    f.close()
    return(False, None)

class Library:
    def __init__(self,bruteforce):
        self.bruteforce = bruteforce
        self.archive = []

    def showarchives(self):
        for archives in self.archive:
            archives.getinfo()
            print("")

    def hackall(self):
        for archives in self.archive:
            if archives.password == None:
                res = self.bruteforce.huck(archive.path)
                if res[0] == True
                    