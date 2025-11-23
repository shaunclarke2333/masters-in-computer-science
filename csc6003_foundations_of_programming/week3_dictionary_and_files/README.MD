# Text Editor Program

This project is a simple text editor program written in Python. It allows the user to load a text file, manipulate its contents through a menu-driven interface, and save changes back to the file.  
The program is designed so that it runs without requiring manual edits to file paths. If an existing file is used, it should be included alongside the program so the file location can be hardcoded. If the program creates a file, it will create it in the same directory as the `.py` file.

## Program Requirements

The text editor must provide the following features:

### 1. `AllWordCount`
Counts the frequency of each word in the file and outputs the **top five most common words**.

### 2. `SingleWordCount`
- Prompts the user to enter a single word.
- Validates that the input contains only one word.
- Outputs the number of times that word appears in the text.

### 3. `ReplaceWord`
- Accepts a target word and a replacement word.
- Replaces all occurrences of the target word.
- Outputs the number of words replaced.

### 4. `AddText`
Appends new text to the existing text stored in the file.

### 5. `DeleteText`
- Accepts a piece of text as input.
- Deletes the **first occurrence** of that text from the file.

### 6. `HighLight`
Highlights all instances of a given word by surrounding them with symbols.

**Example**  
Start text:  
`Hello this is tom and this is ann, we are both students`

Highlighted text for word `this`:  
`Hello **this** is tom and **this** is ann, we are both students`

### 7. `readTextFile`
- Reads the content of the file at program start.
- Stores the text for use in other functions.

### 8. `saveTextFile`
- Saves all changes made to the text.
- Must be called after any modification to ensure updates are written to disk.

## File Handling Notes
- If using an existing file, include it with the program so its path can be hardcoded.
- If creating a new file, it must be created in the same directory as the Python script.
- The program should run successfully without requiring changes to file paths.
