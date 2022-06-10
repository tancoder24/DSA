class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

a = Person("John", "Doe")
a.printname()

########################################################
class Student1(Person):
  pass

b = Student1("Mike", "Olsen")
b.printname()

########################################################
class Student2(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

c = Student2("Tanmay", "Gupta")
c.printname()

########################################################
class Student3(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

d = Student3("Radhe", "Krishna")
d.printname()