class Person:  #SUPER CLASS#

    
###########constructor###############
    def __init__(self, name, DOB):
        self.name = name
        self.DOB = DOB
        
#####################################

        
############SUB CLASS################
class Instructor(Person):

    ##Here Miguel inserted a new variable which was the salary into the
    ##constructor at the end
    def __init__(self, name, DOB, salary):
        super().__init__(name, DOB)
        self.salary = salary

    ##Here Miguel used the __repr__ method to be able to print out
    ##everything with just one print instead of multiple prints
    def __repr__(self):
        return '{self.name}, {self.DOB} , {self.salary}'.format(self=self)


InstructorONE = Instructor('Silvorsky', 1975, 10000)
InstructorTWO = Instructor('Steven' , 1985, 50000)
InstructorTHREE = Instructor('Dave' , 1970, 60000)

print(InstructorONE)
print(InstructorTWO)
print(InstructorTHREE)
