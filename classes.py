class Person:
    species = 'Homosapian'

    def hello(self):
        print("Hello World")

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hi(self):
        print("Hi, my name is " + self.name)


class Student(Person):
    role = 'Student'

tahmauri = Student("Tahmauri", 17)
print(tahmauri.species)
tahmauri.hello()

print(tahmauri.name)
print(tahmauri.age)
tahmauri.hi()

saint = Student("Saint", 17)
print(saint.species)
saint.hello()

print(saint.name)
print(saint.age)
saint.hi()

class Teacher(Person):
    role = 'Teacher'
    def hi(self):
        print("Hi, my name is Mr." + self.name)


forlenza = Teacher("Forlenza", 184)
print(forlenza.role)

forlenza.hi()