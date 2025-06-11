# Music Collection Organizer

## Description

The **Music Collection Organizer** is a Python-based command-line application that allows users to manage personal music libraries. Each user has an individual collection where they can add, update, retrieve, and delete songs. The program supports multi-user functionality and presents interactive menus for navigating through various music-related tasks.

## Features

- **Add User**: Create a new user account. Each user has a unique music collection.
- **Change User**: Switch between existing users or add a new one.
- **Add a Song**: Add a song by specifying its title, artist, and genre.
- **Retrieve Song Details**: Search for a song by title and view the artist and genre.
- **Update Song Details**: Modify the artist and genre of an existing song.
- **Delete a Song**: Remove a song from the user’s collection.
- **Display All Songs**: List all songs in the current user's music collection.

## Project Structure

```bash
.
├── input_handler.py                # Handles all user input and validation
├── main_shaun_clarke_Module4_Project.py  # Main entry point that manages program logic and flow
├── menu.py                         # Dynamically generates menus based on program state
├── user.py                         # Contains User and MusicUser classes with all music library functionality
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/music-collection-organizer.git
   cd music-collection-organizer
   ```

2. Run the application:
   ```bash
   python main_shaun_clarke_Module4_Project.py
   ```

3. Follow the on-screen prompts to interact with the application.

## Requirements

- Python 3.8 or higher

No additional dependencies are required beyond the standard library.

## Author

Shaun Clarke
