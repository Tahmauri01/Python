#asks for the grade the user has
print('Please enter your average: ')
x = int(input())

#Tells the user when their GPA and letter grade is.
if 87 <= x < 100:
    print("Your GPA is 4.0 and your Letter Grade is an A")
elif 77 <= x <= 86:
    print("Your GPA is 3.0 and your Letter Grade is a B")
elif 67 <= x <= 76:
    print("Your GPA is 2.0 and your Letter Grade is a C")
elif 60 <= x <= 66:
    print("Your GPA is 1.0 and your Letter Grade is a D")
else:
    print("Your GPA is 0.0 and your Letter Grade is a F")
