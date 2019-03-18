class Person: #Super Class#

    ######################Constructor########################
    def __init__(self, first, last, DOB):
        self.first = first
        self.last = last
        self.DOB = DOB
    #########################################################

    #####################NAME################################
    def name(self):
        return '{} {}'.format(self.first, self.first)
    #########################################################

    ###########################Birthday######################
    def birthday(self):
        print(DOB)
    #########################################################
        
class Student(Person): #Inheritance#

    def __init__(self, first, last, DOB, major):
        super().__init__(first, last, DOB)
        self.major = major


student_1 = Student('Jeff', 'Bitch', 1945, 'Memeology')
#print statements
print(student_1.first)
print(student_1.last)
print(student_1.DOB)
print(student_1.major)
