
'''
Names in group:
Miguel Salazar, Julio Paveda, Jesus Rodriguez, *RJ Sundseth
Date: 12th March, 2019
Version: 0.0.1
Program description:
++Make a class Employee with a name and salary. 
++Make a class Manager inherit from Employee. 
  Add an instance variable, named _department, that stores a
  string. 
  
++Supply a method __repr__ that prints the manager's name, department, and salary.
  Make a class Executive inherit from Manager. Supply appropriate __repr__ methods 
  for all classes.
  
++Supply a text program that tests these classes and methods.
  
'''

# this program is an inheritance program containing:
# Employee, Manager, and Department classes.
# Julio wrote these classes, definitions, etc.
# This is RJ tidying up and adding comments,
# aiming to get this program easy-to-read and
# follow so that - God forbid! - we ever
# need to come back to it, we'll know how it 
# worked!

## I re-wrote most of the functions myself. However,
## Julio's work helped a lot in getting a better idea
## on how to work flowed.

## As such, I'd say this is a joint-effort for Julio and I
## but I'll do my best to add comments specific to Julio and/or
## my code where applicable



## make a class Employee with a name and salary.
## might as well consider this the ^^superclass^^
## because all the other classes will inheret from
## Employeee

class Employeee(object):
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  def __repr__(self):
        return '{self.name}, {self.salary}' ##.format(self=self)


denise = Employeee("denise", 65000.58)

print(f"Name of employee is: {denise.name}, born\
  like the little hussie that cunt is.")



## now let's make a class Manager that 
##inherits from Employeee
## subclass of Employee called Manager

class Manager(Employeee):
  def __init__(self, name, salary, _department):
    self._department = _department
    super(Manager, self).__init__(name, 80000000)
  def __repr__(self):
    return '{self.name} , {self.salary}, {_department}'
    
class Executive(Manager):
  def __init__(self, name, salary, _department, _executiveImportantHuman):
    self._executiveImportantHuman = _executiveImportantHuman      
    super(Executive, self).__init__(name, salary, _department)
Jessica = Manager("Jessica", 80000, "Management")
print(f"Name of employee is: {Jessica.name}\
  she gets paid {Jessica.salary} per year to be a frigid nightmare\
    of a woman.")

rexRuthless = Executive("Rex Ruthless", 9999999999999999999, "Suuuper Management", "He's a\
   corrupt and horrible person but he has a lot of money, so he gets away with whatever.\
      It's the US, what do you expect?")
print(f"Name of prick CEO is: {rexRuthless.name}. He gets paid an ungodly {rexRuthless.salary}")

# class Executive(Manager):
#   ## make a __repr__ that prints 
#   def __init__(self, name, salary, _department, isExecutive):
#     self.isExecutive = isExecutive
#     super(Manager, self).__init__(name, salary, _department)

#   def __repr__(self):
#         return '{self.name} , {self.salary}, {self._department}'






print(f"The name of our Manager is {Jessica.name} and she's a lazy cunt. We pay her {Jessica.salary} to yell at people and fart all the time. {Jessica._department}")


## this is a bit of code to test out our superclass Employeee with Jimmy
Jimmy = Employeee("Jimmy", 50000)
print(f"Employee name: {Jimmy.name}")
print(f"Employee salary: ${Jimmy.salary} per year")




# ##print(myManager)
# ShitfaceFuckwad = Executive("Mr. Grab her by the Pussy", 800000000000000, "Executive Dept", "CEO" )
# print(f"Our Executive of our company is {ShitfaceFuckwad.name}")

# # class Manager(Employee):
# #   def __init__(self, name, salary):
# #     super(Manager, self).__init__(name, salary)





# # class Employee():
# #     def __init__(self, name, salary):
# #         self.name = name
# #         self.salary = salary

# #     def getName(self):
# #         return self.name

# #     def getSalary(self):
# #         return self.salary

# # Employee()
# # ####### SUB CLASS ##########

# # ## make a class Manager inherit from Employee
# # # class Manager(Employee):
# # #   ##Add an instance variable, named _department, that stores a string.
# # #   ## supply a method __repr__ that prints the manager's name,
# # #   ## department, and salary.
# # #     def __repr__(self, name, salary, _department):
# # #       self._department = ''
# # # ## make a class Executive inherit from Manager. Supply appropriate __repr__ methods 
# # # ## for all classes.
# # # # class Executive(Manager):
# # # #   def repr(self, name, salary, _department):
# # # #     self._department = 'Executive'
    
# # # ## let's make some employees to have fun with!!!!

# # # shitExecutive = Employee()

# # # print(shitExecutive)


# # # ###########################################################
# # # ###########################################################
# # # ## supply a text program that tests these 
# # # ## classes and methods.
# # # ###########################################################
# # # ###########################################################

# # # # print("Alright let's have some fun with this data!")
# # # # name = input("What would you like your low-ranking, shitty-assed\
# # # #   Employee be called? ")

# # # # print("Great, " + name + " Is a fucking banger choice, mate!")
# # # # salary = input("How much money do we think " + name + " should get paid per year? ")

# # # # print("Mkay, thus far" + name + " makes " +)

# # # # print("Now let's promote" + name + "To a manager")
# # # # nameManager = name.