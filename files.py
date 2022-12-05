my_file = open("Tahmauri.txt", "r+")

# print(my_file.readlines())

for line in my_file.readlines():
    print(line, end="........")

print("")
print("")
print("hello")
print("world")

my_file.writelines(['Im writing from python.', ' '])