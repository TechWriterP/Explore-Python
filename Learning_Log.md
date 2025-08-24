# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 1: Band Name Generator

### ✅ What I Learned Today
- [x] Printing strings in Python  
- [x] Taking user input with `input()`  
- [x] String concatenation  

### 🛠️ Project / Exercise
**Project Name:** Band Name Generator  
**Description:**  
- Asks for city and pet name  
- Combines them to generate a fun band name  

**My Code:**  
[Link to my code](./Day01_BandNameGenerator/main.py)

### 💡 Challenges I Faced
- [x] Forgot to add a space between city and pet name → Fixed using `" "`

### 🚀 Extensions / Improvements
- [ ] Add random adjectives to make names cooler  
- [ ] Save generated names to a text file  

### 📖 Resources
- Course Section: Day 1 - Beginner  
- Docs: [Python input()](https://docs.python.org/3/library/functions.html#input)

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 2: Tip Calculator

### ✅ What I Learned Today
- [x] Python primitive data types: int, float, string, and boolean  
- [x] Type conversion with `int()`, `float()`, and `str()`  
- [x] Mathematical operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`  
- [x] Operator precedence (PEMDAS: Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)  
- [x] Rounding numbers with `round(number, 2)`  
- [x] f-Strings for formatted output  

### 🛠️ Project / Exercise
**Project Name:** Tip Calculator  
**Description:**  
- User inputs the bill amount, number of people, and tip percentage (e.g., 10%, 12%, 15%).  
- Program calculates each person’s share including the tip.  

**My Code:**  
[Link to my code](./Day02_TipCalculator/main.py)

### 💡 Challenges I Faced
- [x] Initially forgot to convert input strings into floats/integers  
- [x] Division produced long decimals → solved using `round()` and f-strings  

### 🚀 Extensions / Improvements
- [ ] Allow user to enter any custom tip percentage  
- [ ] Format output with commas for larger bills (e.g., ₹12,345.67)  
- [ ] Add error handling if user enters invalid input  

### 📖 Resources
- Course Section: Day 2 - Beginner: Understanding Data Types and How to Manipulate Strings  
- Docs: [Python round()](https://docs.python.org/3/library/functions.html#round)  
- Docs: [Formatted String Literals (f-strings)](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 3: Treasure Island Game

### ✅ What I Learned Today
- [x] Conditional statements: `if`, `elif`, `else`  
- [x] Nested `if` statements for multi-level decisions  
- [x] Logical operators: `and`, `or`, `not`  
- [x] Importance of indentation in Python  
- [x] Case sensitivity in string comparison  

### 🛠️ Project / Exercise
**Project Name:** Treasure Island Game  
**Description:**  
- A text-based adventure game where the player makes choices to find hidden treasure.  
- Uses conditionals to create different paths and outcomes.  

**My Code:**  
[Link to my code](./Day03_TreasureIsland/main.py)

### 💡 Challenges I Faced
- [x] Forgot to handle upper/lower case inputs → solved using `.lower()`  
- [x] Initially missed proper indentation in nested `if` statements  

### 🚀 Extensions / Improvements
- [ ] Add ASCII art for intro and game-over scenes  
- [ ] Allow replay without restarting program  
- [ ] Add more branches and creative storylines  

### 📖 Resources
- Course Section: Day 3 - Beginner: Control Flow and Logical Operators  
- Docs: [Python if statement](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 4: Rock–Paper–Scissors

### ✅ What I Learned Today
- [x] Python lists and indexing
- [x] Using the `random` module (`randint`, `choice`)
- [x] Comparing user input vs. computer choice
- [x] Handling invalid input gracefully
- [x] Basic game logic and branching

### 🛠️ Project / Exercise
**Project Name:** Rock–Paper–Scissors  
**Description:**  
- Player picks rock/paper/scissors; computer picks randomly.  
- Program prints both choices and declares winner.

**My Code:**  
- [Beginner](./Day04_RockPaperScissors/main.py)  
- [Improved](./Day04_RockPaperScissors/main_plus.py)

### 💡 Challenges I Faced
- [x] Off-by-one errors with list indices → fixed by validating input before indexing
- [x] Handling non-numeric input → wrapped parse with `try/except`

### 🚀 Extensions / Improvements
- [ ] Add score over multiple rounds
- [ ] Offer “best of 5”
- [ ] Keep a simple stats log (wins/losses/draws) to a file

### 📖 Resources
- Course: Day 4 – Randomisation and Python Lists
- Docs: [`random`](https://docs.python.org/3/library/random.html)

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 5: PyPassword Generator

### ✅ What I Learned Today
- [x] Lists: create, index, append, extend
- [x] `for` loops and `range()`
- [x] Randomization with `random.choice()` and `random.shuffle()`
- [x] Joining lists to strings (`"".join(list)`)
- [x] Basic user input validation

### 🛠️ Project / Exercise
**Project Name:** PyPassword Generator  
**Description:**  
- Ask the user how many letters, numbers, and symbols they want.  
- Build a password by randomly picking characters and (optionally) shuffling them.

**My Code:**  
- [Beginner](./Day05_PyPasswordGenerator/main.py)  
- [Improved](./Day05_PyPasswordGenerator/main_plus.py)

### 💡 Challenges I Faced
- [x] Remembering to convert input strings to integers  
- [x] Getting a truly “mixed” password → use `random.shuffle()` before joining

### 🚀 Extensions / Improvements
- [ ] Add strength presets (Weak/Medium/Strong)
- [ ] Add “no ambiguous characters” option (`O/0`, `l/1`, etc.)
- [ ] Copy-to-clipboard (for GUI version later with Tkinter)

### 📖 Resources
- Course: Day 5 – Python Loops
- Docs: [`random`](https://docs.python.org/3/library/random.html)

