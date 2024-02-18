from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
    @staticmethod   # static method is not bound to the class
    def isAdult(age):
        return age > 18
    
person1 = Person("joe", 19) # create a simple object
print(person1)
person2 = Person.fromBirthYear('joe', 1996) 
print(person1.age)
print(person2.age)  # we get age from 2024 (current year) - 1996 = 28

print(Person.isAdult(15))
print(Person.isAdult(19))   




from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass
class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")
class Pentagon(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides") 
class Hexagon(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides") 
  
class Quadrilateral(Polygon): 
    # overriding abstract method 
    def noofsides(self): 
        print("I have 4 sides") 

    
        R = Triangle()
        R.noofsides()

K = Quadrilateral()
K.noofsides() 
  
R = Pentagon() 
R.noofsides() 
  
K = Hexagon() 
K.noofsides() 
