my_file = open("Todo.txt", "a")

todo = []

while True:
    print("Your Todo list is " + " then ".join(todo))
    things = input()
    
    todo.append(things)

    

    my_file.writelines(things + " \n")
    my_file.close()
    my_file = open('Todo.txt', 'a')