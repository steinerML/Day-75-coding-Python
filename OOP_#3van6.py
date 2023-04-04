from dateutil.parser import parse #import dateparser

#class creation and invisible attribute (_name,_sex,_birth) initialization
class Persoon:
    def __init__(self,name,sex,birth):
        self.name = name
        self.sex = sex
        self.birth = parse(birth).date()

#We expand the class definition by defining the following methods.

    def getName(self):
        return self.name
    def getBirth(self):
        return self.birth
    def isMan(self):
        if self.sex == 'M':
            return True
        return False
    def isVrouw(self):
        if self.sex == 'V':
            return True
        return False

# if __name__ == '__main__':

john = Persoon('John','M','18/10/1984')

print(john.getName())
print(john.getBirth())
print(john.isMan())
print(john.isVrouw())