class Person:
    species = 'Homosapian'

    def hello(self):
        print("Hello World")

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hi(self):
        print("Hi, my name is " + self.name)



tahmauri = Person("Tahmauri", 17)
print(tahmauri.species)
tahmauri.hello()

print(tahmauri.name)
print(tahmauri.age)
tahmauri.hi()

saint = Person("Saint", 17)
print(saint.species)
saint.hello()

print(saint.name)
print(saint.age)
saint.hi()