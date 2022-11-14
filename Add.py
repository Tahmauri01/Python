#asks for the number that the user gives
number = int(input())
number2 = int(input())
#adds up the numbers the user gives
number3 = int(number + number2)

#tells what the sum of your numbers are
print("Your result is " + str(number3))

#tells if your number is greater than or less than 10 or less than 0
if number < 10:
    print("Your number is less than 10")
elif number < 0:
    print("Your number is negative")
else:
    print("Your number is not less than 10")