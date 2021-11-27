class Medico:
    def __init__(self, fname, lname, lage):
        self.firstname = fname
        self.lastname = lname
        self.age = lage
        

    def printname(self):
        print(self.firstname, self.lastname,self.age)
        
class Student(Person):
    def __init__(self, fname, lname, lage,lyearingress):
        super().__init__(fname, lname,lage)
        self.yearingress = lyearingress
    
    def printname(self):
        print("nombre: "+ self.firstname+" "+  self.lastname+" edad: "+str(self.age))

class profesional(Person):
    def __init__(self, fname, lname, lage,lcareer):
        super().__init__(fname, lname,lage)
        self.career = lcareer

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe","36")
x.printname()
y = Student("marisol","cruz","22","2016")
y.printname()
z = profesional("raul","vergara","45")
z.printname()