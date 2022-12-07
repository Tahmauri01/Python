try:
    age = int(input('Enter your age: '))
    faveNum = int(input('What is your favorite number: '))
    if age <= 21:
        print('You are not allowed to enter, you are too young.')
    else:
        print('Welcome, you are old enough.')

    print("Fun Fact! Your age divided by your favorite number is: " , age / faveNum)
except ValueError:
    print("Please input a number!")
except ZeroDivisionError:
    print("Your favorite number is not divisible by zero!")
finally:
    print("Wow, you may not an ID-10-T!")
