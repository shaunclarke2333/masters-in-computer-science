# Number Guessing Game – Program Requirements

## Overview
Compose a program that generates a random number for the user to guess.  
The program must be modular and organized using **functions**, **parameters**, and **return values**.  
No function should print directly unless it is for testing. All user-facing output must come from `main()` or wherever the functions are initially called.

Use `import random` to generate your random numbers.

This README also requires a **written algorithm** and a **flowchart** representing your program's logic, including labeled decision paths and loops.

---

## Program Requirements

### 1. Generate Random Number
- Use a function named `generate_random_number()`.
- The function must return a random integer between **1 and 100**.

### 2. User Guess Loop
- Continuously prompt the user to enter a guess.
- Loop until the correct number is guessed.

### 3. Guess Checking
- Use a function named `check_guess(random_number, user_guess)`.
- It returns whether the user's guess is:
  - Correct  
  - Incorrect  
- `main()` displays the appropriate message.

### 4. Basic Hints
- If the guess is incorrect:
  - Tell the user whether the correct number is **higher** or **lower**.

### 5. Additional Hints After 2 Wrong Attempts
After **two incorrect guesses**, provide an extra hint.  
Select one hint **at random** from the following:

- Whether the number is **even or odd**
- Whether the number is a **multiple of 5**
- Whether the number squared (`n^2`) is **greater or less than 1,000**

### 6. Continue Until Correct
- Repeat steps 2 through 5 until the correct guess is made.

### 7. Completion Output
- Once guessed correctly, display:
  - The correct number  
  - The total number of attempts  

---

## Algorithm (Written Description)

1. Start the program.
2. Call `generate_random_number()` to obtain a target number between 1 and 100.
3. Initialize an `attempts` counter to 0.
4. Loop:
   - Prompt the user to enter a guess.
   - Increase `attempts` by 1.
   - Pass the guess to `check_guess()`.
   - If correct:
     - Exit the loop.
   - If incorrect:
     - Tell the user whether the target number is higher or lower.
     - If attempts ≥ 2:
       - Randomly choose and present an additional hint (even/odd, multiple of 5, or n² relative to 1,000).
5. When the user guesses correctly:
   - Display the correct number.
   - Display the number of attempts made.
6. End program.
