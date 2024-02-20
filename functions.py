def print_todos(filename):
    file=open(filename)
    todos = file.readlines()
    file.close()
    for index, item in enumerate(todos):
        item = item.strip("\n")
        row = f"{index + 1} - {item}"
        print(row)
def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos
def write_todos(todos):
    with open('todos.txt', 'w') as file:
        file.writelines(todos)
    return todos
# def update_todos(todo):
#     with open('../files/todos.txt', 'r') as file:
#         todos = file.readlines()
#         todos.append(todo)
#     write_todos(todos)
#     return todos

