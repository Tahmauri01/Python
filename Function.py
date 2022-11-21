#First Function
def helloWorld():
    print('Hello World')

#calls the function
helloWorld()

#Functions to add divide subtract and find remainder
def add(a, b):
    print(a + b)

def subtract(a, b):
    print(a - b)

def divide(a, b):
    print(a / b)

def remainder(a, b):
    print(b % a)
    
#calls each function
add(9, 10)
subtract(9,10)
divide(9, 10)
remainder(9, 10)

x = add(9, 10)

print(x)

#returns the equation instead of printing it
def slope(m, x, b):
    return((m * x) + b)

y = slope(5, 2, 3)


print(y)
