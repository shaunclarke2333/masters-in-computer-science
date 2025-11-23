# Folder System Project

This project implements a `Folder` class that represents a folder in a simplified file system.  
Each folder can contain files (represented as strings) and subfolders (other `Folder` objects).  
The project requires recursive methods to calculate total files, compare folders, and display the folder structure.  
A flowchart and algorithm should also be included.

---

## Folder Class Overview

A `Folder` object includes:

- **name**: The folder's name (string)  
- **files**: A list of file names (strings)  
- **subfolders**: A list of `Folder` objects  

---

## Required Methods

### `add_file(file_name)`
Adds a file (string) to the current folder.

### `add_subfolder(folder_object)`
Adds a subfolder (another `Folder` object) to the current folder.  
Folder names must be unique.

### `select_folder(folder_name)`
Selects a subfolder by name and makes it the *current* folder from which operations continue.

### `__count_files()`  
Private, recursive method.  
Counts and returns the total number of files in the folder and all nested subfolders.

### `__eq__(other)`
Compares the folder to a string.  
Returns `True` if the string matches the folder's name.

### `__len__()`
Returns the total number of files contained in the folder and all nested subfolders.

### `__str__()`
Returns a formatted string representation of the folder:  
- Folder name  
- List of files  
- Indented subfolders for visual hierarchy  
There should be a menu option that prints this representation.

---

## Additional Requirements

- The project should include an **algorithm description** and a **flowchart** showing the recursive structure and method interactions.
- All folder names must remain unique across the system.

