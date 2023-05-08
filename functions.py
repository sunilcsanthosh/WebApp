def get_todos(filepath = "todos.txt"):
    """ Read a text file and retun the list of to do items """
    with open(filepath,'r') as file:   # No need to close the filesdf
        todos = file.readlines()  # todos is of type list 
    return todos

def write_todos(todos,filepath = "todos.txt"):
    with open(filepath,'w') as file:
        file.writelines(todos)

print(__name__)
if __name__== "__main__":
    print("Function is excuded directely")