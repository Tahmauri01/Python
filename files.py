my_file = open("Tahmauri.txt", "a")

# print(my_file.readlines())

my_file.write('\nIm writing from python.')

my_file.close()

my_file = open('Tahmauri.txt')

for line in my_file.readlines():
    print(line, end="|")

print("")
print("")
print("hello")
print("world")

