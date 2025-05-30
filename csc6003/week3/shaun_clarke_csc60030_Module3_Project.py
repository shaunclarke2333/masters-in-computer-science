import string
import re


# Global file path variable
file_path = "other_file.txt"

# This function closes the file if it is open
def close_file(file):
    """
    This function this function closes the .txt file.<br>
    
    parameters:<br>
    - file:<br>
      - This parameter is the .txt file thats open.<br>
    
    returns:<br>
      - This function returns nothing.<br>
    """

    file.close()

# This function reads the file content
def read_file(path, no_case=False):
    """
    This function reads in the contents of a .txt file.<br>
    Then converts everything to lower case.<br>
    
    parameters:<br>
    - [string] path:<br>
      - This parameter is the path to the .txt file
    - [bool] no_case=False:<br>
      - Defaul parameter that allows you to skip changing the file case.
    
    returns:<br>
      - This function returns the contents of the .txt file as a string.<br>
      - Returns false if the file was not found
    """

    try:
        # Opening the text file
        file = open(path)
        # Local variable to hold the contents of the file
        file_content = file.read()
        # Closing the file
        close_file(file)

        if not no_case:
            # Converting the file contents to lower case
            file_content = file_content.lower()
        return file_content
    except FileNotFoundError as err:
        return False
    
# This function writes content to the file
def write_to_file(path,mode,content):
    """
    This function writes content to the .txt file.<br>
    
    parameters:<br>
    - [string] path:<br>
      - Path to the .txt file
    - [string] mode:<br>
      - This the mode when opening the text file for writing.
      - 'a' for append and 'w' for write.
    - [string] content:<br>
      - This is the content that will be written to the .txt file

    
    returns:<br>
      - File content as a string.<br>
      - Returns False if the file wa snot found.<br>
    """

    try:
        # Opening file
        file = open(path, mode, newline="")
        
        # Logic to handle if we want to append or overwrite
        if mode == "a":
            file.write(f"\n{content}")
        if mode == "w":
            file.write(content)
        
        # Closing the file
        close_file(file)

        # reading the contents from the file
        file_content = read_file(path)
        return file_content
    except FileNotFoundError as err:
        return False

# This function removes punctuations from the text file data
def remove_punctuations(file_content, split=True):
    """
    This function removes punctuations from the text file data.<br>

    parameters:<br>
    - [string] file_content:<br>
      - The output of the read file function
      - Which is usually the contents of the text file as a string.
    - [string] split=Flase:<br>
      - Default parameter that Allows user to skip split.

    returns:<br>
      - Returns the file content as a lsit.<br>
    """

    # creating dictionary of punctuations to replace
    translator = str.maketrans("", "", string.punctuation)
    # removing punctuatiosn from file
    file_content = file_content.translate(translator)

    if split:
        # Turning string into a list
        file_content = file_content.split()
    
    return file_content

# This function returns the fice nmost common words
def all_word_count(path):
    """
    This function reads in the content of a .txt file.<br>
    
    parameters:<br>
    - path:<br>
      - This parameter is the path to the .txt file
    
    - returns:<br>
      - This function returns a list of tuples with the 5 most common words and the total times they appeared.<br>
      - Returns **False** if the file was not found.
    """
    try:
        # Empty dict to hold words and their count
        counting_dict = {}
        # Empty list to hold words and their counts
        list_of_values = list()

        # reading file content
        file_content = read_file(path)

        # Removing punctuations
        file_content = remove_punctuations(file_content)

        # getting each word and number of times it appears to a dictionary
        for word in file_content:
            if word not in counting_dict:
                counting_dict[word]= 1
            elif word in counting_dict:
                counting_dict[word] += 1

        # Converted dictionary to list a of tuples and looping through it.
        for key, value in list(counting_dict.items()):
            list_of_values.append((value, key))

        #sorting list by totals in descending order
        list_of_values.sort(reverse=True)

        # returning the first five items in the sorted list
        return list_of_values[:5]
    except FileNotFoundError as err:
        return False

# This function tells us how many time a word appears in the document
def single_word_count(path, word):
    """
    This function finds out how many times a single word appeared in the .txt document.<br>
    
    parameters:<br>
    - path:<br>
      - This parameter is the path to the .txt file
    - word:<br>
      - This word would be submitted by the user 
      
    - returns:<br>
      - This function returns an integer for the number of times the word appeared<br>
      - if the word submitted doesn't exist, it returns false.
      - Returns **not found** if the word or text is not in the file.
      - Returns **file not found** if the file was not read.
    """
    try:
        # local variable for file content
        file_content = read_file(path)

        file_content = remove_punctuations(file_content)
   
        if word not in file_content:
            return 0

        # local variable for word count
        word_freq = file_content.count(word)
        return word_freq
    except FileNotFoundError as err:
        print(err)
        return "file not found"

# This function replaces a word or a line of text in the file
def replace_item(path, item_to_replace, new_item, skip=False):
    """
    This function replaces a word or a line of text in the file.<br>
    
    parameters:<br>
    - [string] path:<br>
      - Path to the .txt file
    - [string] item_to_replace:<br>
      - The word or text to replace.
    - [string] new_item:<br>
      - The new word or text that will be added to the file.
    - [string] skip=Flase:<br>
      - Dedault parameter. We set to true if we are
      Calling this function to delete an item.

    
    returns:<br>
      - Returns **0** if the word or text is not in the file.
      - Returns **not updated** if file was not updated.
      - Returns **False** if the file was not found.<br>
    """
    try:
        # Local variable to hold how many times the word appears before change
        old_word_count = single_word_count(path, item_to_replace)

        # If word does not exist return false
        if old_word_count == 0:
            return 0

        # local variable to hold file content
        file_content = read_file(path)

        file_content = remove_punctuations(file_content,split=False)

        # Local variable to hold the regex pattern to find the whole word
        pattern = rf'\b{item_to_replace}\b'
        # local variable to hold updated file content output using regex to maintain punctuation
        updated_file_content = re.sub(pattern, f'{new_item}', file_content)

        # Writing updated content back to the text file
        write_to_file(path,"w",updated_file_content)

        # Local variable to hold new word count 
        new_word_count = single_word_count(path,item_to_replace)
        print(f"New word count{new_word_count}")

        # Skipping this logic because we are deleting a word and not replacing it
        if not skip:

            if old_word_count == new_word_count:
                return "not updated"

            if new_word_count == 0:
                return old_word_count
        
        # Not skipping when we are deleting a word
        if skip:
             if new_word_count == 0:
                return old_word_count

    except FileNotFoundError as err:
        return False

# This function adds text to a file
def add_text(path, mode,content):
    """
    This function finds out how many times a single word appeared in the .txt document.<br>

    parameters:<br>
    - [string] **path**:<br>
      - Path to the .txt file
    - [string] mode:<br>
      - This is the mode when opening the text file for writing.
      - 'a' for append and 'w' for write.
    - [string] content:<br>
      - This is the content that will be written to the .txt file
      
    - returns:<br>
      - This function returns The content of the text file after it has been written to.
      - Returns **False** if the file was not read.
    """
    try:
        # Write content to file
        file_content = write_to_file(path, mode,content)
        return file_content
    except FileNotFoundError as err:
        return False
    
# This function deletes a word or text from the file
def delete_text(path, item_to_replace):
    """
    This function deletes a word or text from the file.<br>
    
    parameters:<br>
    - [string] path:<br>
      - Path to the .txt file
    - [string] item_to_replace:<br>
      - The word or text to replace.
    
    returns:<br>
      - Returns the number of items that were deleted.
      - Returns **not found** if the item to delete does not exist.
      - Returns **False** if the file was not found.<br>
    """
    try:
        # Read content from file
        file_content = read_file(path)

        # Checking if file content exists
        if not file_content:
            return "not found"

        # Deleting the word or text from the file.
        updated_item = replace_item(path, item_to_replace, new_item="", skip=True)

        # Confirming if the fiel was updated
        if updated_item == "not found" or updated_item == "not updated":
            return False

        return updated_item
    except FileNotFoundError as err:
        return False

# This function highlights text selected by the user
def highlight_text(path, item_to_highlight):
    """
    This function highlights text selected by the user.<br>
    
    parameters:<br>
    - [string] path:<br>
      - Path to the .txt file
    - [string] item_to_highlight:<br>
      - The word or text to highlight.

    
    returns:<br>
      - Returns the number of items that were deleted.
      - Returns **not found** if the word or text is not in the file.
      - Returns **False** if the file was not found.<br>
      - Returns **False** if the file was not updated.<br>
      - Returns **exists** if the highlight already exists in file.<br>
    """
    try:
        file_content = read_file(path)

        if not file_content:
            return "not found"
        
        highlighted_item =f">>{item_to_highlight}<<"
        
        if highlighted_item in file_content:
            return "exists"

        updated_item = replace_item(path, item_to_highlight,highlighted_item)

        if updated_item == 0 or updated_item == "not updated":
            return False

        return updated_item
    except FileNotFoundError as err:
        return False
    
# This fucntion gets user input
def get_user_input(input_message, path, new=False):
    """
    This function gets the user inputs for the menu.<br>
    Parameters:<br>
    - input_message
      - A message telling the user what kind of input to enter.
   - path:<br>
      - This parameter is the path to the .txt file
   - new=False<br>
      - This is a default parameter that if false allows us to accept an input that is not in the file.
      
    Returns:<br> 
    - The user input.<br>
    """
    
    while True:
        try:
            # Getting the user input
            user_input = input(f"\n{input_message}\n:> ").lower()

            # Getting content from text file
            file_content = read_file(path)
            
            if not new:
                if user_input not in file_content:
                    raise ValueError(f"\nInvalid input *{user_input}* not found in file.\n")
        
            return user_input
        except ValueError as err:
            print(err)
            continue


# This function accepts the user_menu input
def user_menu_input():
    """
    This function gets the user inputs for the menu.<br>
    Parameters:<br>
    - This function takes no parameters
      
    Returns:<br> 
    - The user input as an integer.<br>
    """
    
    
    while True:
        try:
            # Asking the user to eneter their menu selection
            user_input = int(input(
            f"""\n=+=+=+=Text Editor Menu=+=+=+=\n1: Top 5 most common words\n2: Single Word Frequency\n3: Replace a word\n4: Add Text\n5: Delete Text\n6: Highlight Text\n7: Undo all changes\n\nPlease Select a Menu Option\n:> """
            ))

            # Logic to validate user input and proceed accordingly. 
            if user_input >= 1 and user_input <= 8:
                return user_input
            else:
                raise ValueError(f"\nPlease enter a valid input\n")
        except ValueError as err:
            print(f"\n{err}")
            print(f"Please enter a valid input\n")

# Bringing it all together
def main(path):

    # Getting file content before any changes
    original_file_content = read_file(path, no_case=True)

    while True:
        # Calling user menu
        menu_input = user_menu_input()

        # Using match to trigger edit features based on user input
        match menu_input:
            case 1:
                # Getting the five most common words and their counts
                top_five_words = all_word_count(file_path)

                # Displaying top five words details
                print(f"\nThe top five words are as follows:\n")
                for i in range(len(top_five_words)):
                    # Capitalizing the first letter of each word
                    word = top_five_words[i][1].title()
                    # Getting the count for each word
                    word_count = top_five_words[i][0]
                    print(f"*{word}* appeared {word_count} time{'s' if word_count != 1 else ''}.")
            case 2:
                # Getting user input for word they want to count
                user_word_input = get_user_input("Please enter the word you would like to count", path)
                # Removing punctuations
                user_word_input = remove_punctuations(user_word_input,split=False)
                # Getting the word count
                word_count = single_word_count(path, user_word_input)
                print(f"\nThe word '{user_word_input.capitalize()}' appears {word_count} time{'s' if word_count != 1 else ''}.\n")
            case 3:
                # Getting user input for words they would like to replace
                item_to_replace = get_user_input("Please enter the word you would like to replace.", file_path)
                # Removing punctuations
                item_to_replace = remove_punctuations(item_to_replace,split=False)

                new_item = get_user_input("Please enter the new word.", file_path, new=True)
                # Removing punctuations
                new_item = remove_punctuations(new_item,split=False)
                # Replacing word that user selected
                updated_word_count = replace_item(file_path,item_to_replace,new_item)
                print(f"\nThe word '{item_to_replace.capitalize()}' was replaced with '{new_item.capitalize()}' in {updated_word_count} place{'s' if updated_word_count != 1 else ''}\n")
            case 4:
                # Getting user input for text they would like to add
                text_to_add = get_user_input("Please enter the text you would like to add", file_path, new =True)

                # Adding the text to the file
                text_added = add_text(file_path, "a", text_to_add)
                print(f"\n'{text_to_add}' was added to {file_path}\n")
                print(text_added)
            case 5:
                # Getting user input for the item they want to delete:
                item_to_delete = get_user_input("Please enter the text you would like to delete.", path)
                # Removing punctuations
                item_to_delete = remove_punctuations(item_to_delete,split=False)

                # Deleteing text from file
                deleted_text = delete_text(file_path,item_to_delete)

                print(f"\n'{item_to_delete.capitalize()}' was deleted from {deleted_text} place{'s' if deleted_text != 1 else ''}\n")
            case 6:
                # Getting user input for text they would like to highlight.
                text_to_highlight = get_user_input("Please enter the text you would like to highlight", path)
                # Removing punctuations
                text_to_highlight = remove_punctuations(text_to_highlight,split=False)
                # Highlighting text
                highlighted_text = highlight_text(file_path,text_to_highlight)

                # If text is already highlighted
                if highlighted_text == "exists":
                    print(f"{text_to_highlight.capitalize()} is already highlighted.")

                    file_content = read_file(file_path)
                    print(file_content)
                    continue
                    
                print(read_file(file_path))
            case 7:
                # Writing original file content back to file before modifications
                write_to_file(path, "w",original_file_content)

                # reading and displaying updated file
                file_content = read_file(file_path, no_case=True)
                print(file_content)
            case 8:
                print(f"\nSafe travels on your journey\n")
                exit()

print(main(file_path))