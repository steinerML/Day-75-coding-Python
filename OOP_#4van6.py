from dateutil.parser import parse #import dateparser
from datetime import *

#class creation and attribute initialization
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
        else:
            return False
    def isVrouw(self):
        if self.sex == 'V':
            return True
        else:
            return False
    def age(self):
        age = date.today() - self.birth
        return age//timedelta(days=365)

if __name__ == '__main__':

    john = Persoon('John','M','18/10/1984')

    print(john.getName())
    print(john.getBirth())
    print(john.isMan())
    print(john.isVrouw())
    print(john.age())