
# This function allow syou to interact with a file
def handle_file(path, action, mode, content=None,word_to_replace=None,word_to_add=None):

    if action == "read" and mode == "r":
        with open(path, mode) as file:
            file_content = file.read()
            file_content.lower()
            return file_content
    elif action == "write" and mode == "a":
        with open(path, mode) as file:
            file.write(content)

        with open(path, "r") as file:
            file_content = file.read()
        return file_content
    elif action == "repalce":
        with open(path, mode) as file:
            file_content = file.read()
        file_content.lower()
        file_content = file_content.replace(word_to_replace, word_to_add)
        print(file_content)

        with open(path, "w") as file:
            file_content = file.write(file_content)
            
        with open(path, "r") as file:
            file_content = file.read()
            return file_content
            
# This function replaces 
    

# File path
file_path = "other_file.txt"

# lets_see = handle_file(file_path, "read", "r")
lets_see = handle_file(file_path, "write", "a",content="\nSome more new stuff")
# lets_see = handle_file(file_path, "read", "r", word_to_replace="this",word_to_add="that")
print(lets_see)