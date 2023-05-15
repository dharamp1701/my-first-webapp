FILEPATH = "todos.txt"

def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)

print("__main__")
if __name__ =="__main__":
    print('hello')

    print(get_todos())

