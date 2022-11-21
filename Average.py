

print('Please enter your grades')
a = input()
b = input()
c = input()
d = input()

x  = [a, b, c, d]

sum = 0

for grade in x:
    sum = sum + int(grade)

print(str(sum/len(x)) + '%')

