# Battleship Variation Project

This project implements a simplified version of the classic board game **Battleship**.  
Instead of two players, you will place 5 ships randomly on a 10×10 grid, and the computer (user input) will guess coordinates until all ships are sunk.

Each ship occupies a single square for simplicity.

---

## Overview

You will use a two-dimensional array (list of lists) to represent the game board.  
Five ships (`S`) are randomly placed on the grid. The player will repeatedly guess a column and row until all ships are sunk.

The board displays the following characters:

- `.` — Empty square, not yet guessed  
- `S` — Ship  
- `O` — Miss (guessed but no ship)  
- `X` — Hit (ship found)

---

## Required Functions

### **1. drawBoard(board)**
Displays the 10×10 game board.

- Columns appear left-to-right, rows top-to-bottom.
- Numbers `0–9` must appear along the top and left for reference.
- Shows `.`, `S`, `O`, or `X` depending on square state.

---

### **2. isGameOver(board)**
Returns `true` if all ships have been hit (all `S` → `X`).  
Returns `false` otherwise.

---

### **3. setupBoard()**
Creates and initializes the board:

- Start with a 10×10 grid filled with `.`  
- Randomly place `NUM_SHIPS` ships (`S`) on unique squares  
- Continue generating coordinates until all ships are placed without overlap  

---

### **4. checkHitOrMiss(board, col, row)**
Checks the player’s guess and updates the board:

- If the square contains `S`, change to `X` and return `"HIT"`  
- If the square already contains `X`, return `"HIT"`  
- Otherwise, change square to `O` and return `"MISS"`

---

## Main Program Requirements

Your `main` function should:

1. **Set up the game board**
2. **Draw the board and prompt for a column (X)**
   - If invalid (`< 0` or `>= 10`), print `"Invalid column"` and ask again
3. **Draw the board and prompt for a row (Y)**
   - If invalid, print `"Invalid row"` and ask again
4. **Check hit or miss**
   - Print `"HIT"` or `"MISS"`
   - Update board with `O` or `X`
5. **Check if all ships are sunk**
   - If yes:  
     - Draw the board  
     - Print `"GAME OVER!"`  
     - End program
6. **Otherwise repeat from Step 2**

---

## End Condition

The game continues until all ships have been hit and the board contains no remaining `S` characters.

---
