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

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 26: NATO Alphabet Project

### ✅ What I Learned Today
- [x] Python **list comprehensions** for quick list creation  
- [x] **Dictionary comprehensions** for transforming data  
- [x] Reading CSV files with **Pandas**  
- [x] Iterating over Pandas DataFrames (`iterrows()`)  
- [x] Handling user input with **exception handling** (`try/except`)  
- [x] Converting strings into lists (`list(string)` and `[letter for letter in word]`)  

### 🛠️ Project / Exercise
**Project Name:** NATO Alphabet Project  
**Description:**  
- Read a CSV file (`nato_phonetic_alphabet.csv`) into a Pandas DataFrame.  
- Convert it into a dictionary mapping each letter to its NATO code word.  
- Ask the user for a word and output the NATO code words for each letter.  
- Handle invalid inputs (non-alphabet characters).  

**My Code:**  
[Link to my code](./Day26_NATOAlphabet/main.py)

### 💡 Challenges I Faced
- [x] Forgetting `.upper()` when matching input with dictionary keys  
- [x] Handling non-alphabet characters (numbers/symbols) without crashing → solved with `try/except` and recursion  

### 🚀 Extensions / Improvements
- [ ] Accept full sentences (ignore spaces and punctuation)  
- [ ] Export generated NATO words to a `.txt` file  
- [ ] Add an option to pronounce words using `pyttsx3` (text-to-speech)  

### 📖 Resources
- Course: Day 26 – NATO Alphabet Project  
- Docs: [Pandas DataFrame.iterrows()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)  
- Docs: [Python List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 27: Tkinter and GUI Programs

### ✅ What I Learned Today
- [x] Introduction to **Tkinter**, Python’s built-in GUI library  
- [x] Creating a window with `Tk()`  
- [x] Adding **labels**, **buttons**, and **entry fields**  
- [x] Using `.pack()`, `.place()`, and `.grid()` for widget layout  
- [x] Updating label text dynamically with `.config()`  
- [x] Getting user input from `Entry()` fields with `.get()`  
- [x] Using functions as button callbacks (event-driven programming)  

### 🛠️ Project / Exercise
**Project Name:** Mile to Kilometer Converter  
**Description:**  
- Simple GUI app using Tkinter.  
- User enters miles in a text box, clicks a button, and sees the equivalent in kilometers displayed.  

**My Code:**  
[Link to my code](./Day27_MileToKmConverter/main.py)

### 💡 Challenges I Faced
- [x] Forgetting to call `mainloop()` → window didn’t stay open  
- [x] Mixing up `.pack()` and `.grid()` in the same window → caused errors  
- [x] Not converting `Entry.get()` (string) to float before doing math  

### 🚀 Extensions / Improvements
- [ ] Add conversion in both directions (Miles → KM, KM → Miles)  
- [ ] Add input validation (only allow numbers)  
- [ ] Improve UI with padding, fonts, and colors  

### 📖 Resources
- Course: Day 27 – Tkinter, *args, kwargs, and GUI Programs  
- Docs: [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)  
- Tkinter Layouts: [pack vs grid](https://tkdocs.com/tutorial/grid.html)

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 28: Pomodoro Timer App

### ✅ What I Learned Today
- [x] More practice with **Tkinter widgets** (labels, buttons, canvas)  
- [x] Using the **Canvas widget** to display images and text  
- [x] Tkinter **`after()` method** for scheduling functions (like a timer)  
- [x] Canceling scheduled events with `.after_cancel()`  
- [x] Implementing **countdown timers** with recursion-style functions  
- [x] Understanding the **Pomodoro Technique** (25-5-25-5-25-5-25-15 cycle)  
- [x] Using global constants for settings (work time, short break, long break)  

### 🛠️ Project / Exercise
**Project Name:** Pomodoro Timer  
**Description:**  
- A Tkinter app that runs a productivity timer.  
- Counts down work sessions (25 min), short breaks (5 min), and long breaks (15 min) after 4 cycles.  
- Displays checkmarks ✅ after each completed session.  

**My Code:**  
[Link to my code](./Day28_PomodoroTimer/main.py)

### 💡 Challenges I Faced
- [x] Forgetting to use `global` keyword for variables modified inside functions  
- [x] Understanding how `.after()` works differently from `time.sleep()`  
- [x] Resetting the timer correctly without overlapping scheduled calls  

### 🚀 Extensions / Improvements
- [ ] Add a **Pause/Resume** button  
- [ ] Allow user to set custom work/break durations  
- [ ] Play a sound notification when timer ends  
- [ ] Improve UI with colors, fonts, and icons  

### 📖 Resources
- Course: Day 28 – Tkinter, Dynamic Typing, and the Pomodoro GUI App  
- Docs: [Tkinter Canvas](https://tkdocs.com/tutorial/canvas.html)  
- Pomodoro Technique: [Official Site](https://francescocirillo.com/pages/pomodoro-technique)

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 29: Password Manager GUI App (Part 1)

### ✅ What I Learned Today
- [x] Tkinter **Entry widgets** for user input  
- [x] Tkinter **Label and Button widgets** for layout  
- [x] Generating random strong passwords (reuse logic from Day 5 project)  
- [x] Adding a **Copy to Clipboard** feature using `pyperclip`  
- [x] Writing user data (website, email/username, password) to a `.txt` file  
- [x] Using `.delete(0, END)` to clear Entry fields after saving  

### 🛠️ Project / Exercise
**Project Name:** Password Manager (GUI)  
**Description:**  
- Tkinter-based app for storing passwords.  
- User enters a website, email/username, and password.  
- App can generate a random password and copy it to clipboard.  
- Data is saved to a text file (`data.txt`).  

**My Code:**  
[Link to my code](./Day29_PasswordManager/main.py)

### 💡 Challenges I Faced
- [x] Forgetting to strip input values before saving → fixed with `.get().strip()`  
- [x] Handling empty fields (website/email/password) → solved by adding simple validation  
- [x] Ensuring password was copied automatically → solved with `pyperclip.copy(password)`  

### 🚀 Extensions / Improvements
- [ ] Save data in **JSON format** (to allow retrieval by website)  
- [ ] Add a search feature to look up saved credentials  
- [ ] Add error handling when saving/loading files  
- [ ] Improve UI (grid padding, alignment, colors)  

### 📖 Resources
- Course: Day 29 – Building a Password Manager GUI App with Tkinter  
- Docs: [Tkinter Entry](https://tkdocs.com/tutorial/widgets.html#entry)  
- Docs: [pyperclip](https://pypi.org/project/pyperclip/)  
- Python File I/O: [open()](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 30: Password Manager with Error Handling and JSON Data

### ✅ What I Learned Today
- [x] Writing and reading data in **JSON format** using the `json` module  
- [x] Updating JSON data without overwriting existing entries  
- [x] Using **try/except** blocks for error handling (e.g., file not found)  
- [x] Nested `try/except` for handling missing keys in JSON data  
- [x] Using `dict.update()` to merge new data into existing JSON file  
- [x] Exception handling best practices: specific exceptions > bare `except`  

### 🛠️ Project / Exercise
**Project Name:** Password Manager (Enhanced with JSON + Error Handling)  
**Description:**  
- Save and retrieve credentials in a `data.json` file.  
- Each website is stored as a key, with values for email/username and password.  
- Handle missing JSON file gracefully by creating one automatically.  
- Add a **search feature**: user enters a website name, app shows stored credentials if found.  

**My Code:**  
[Link to my code](./Day30_PasswordManager_JSON/main.py)

### 💡 Challenges I Faced
- [x] Forgetting to open JSON file in read mode before updating → fixed by using `with open("data.json", "r")`  
- [x] `json.decoder.JSONDecodeError` when file was empty → solved by initializing with an empty dict `{}`  
- [x] KeyError when searching for a website not in data → fixed with `if website in data:`  

### 🚀 Extensions / Improvements
- [ ] Mask passwords in UI (show as dots but allow reveal button)  
- [ ] Add a “Copy Password” button directly in search results  
- [ ] Implement secure encryption before saving (using `cryptography` library)  
- [ ] Sync data with cloud storage (Google Drive/Dropbox API)  

### 📖 Resources
- Course: Day 30 – Errors, Exceptions, JSON Data, and Improving the Password Manager  
- Docs: [Python json module](https://docs.python.org/3/library/json.html)  
- Error Handling: [try/except](https://docs.python.org/3/tutorial/errors.html)  
- Best Practice: [Don’t use bare except](https://realpython.com/the-most-diabolical-python-antipattern/)

# 🐍 100 Days of Code - Python Bootcamp (Angela Yu)

## 📅 Day 31: Flashcard Capstone Project

### ✅ What I Learned Today
- [x] Using **Tkinter Canvas** to display images and text dynamically  
- [x] Layering canvas elements (background + text on top)  
- [x] Tkinter `.after()` for timed card flips (e.g., 3 seconds)  
- [x] Working with **Pandas DataFrame** to load CSV files  
- [x] Converting DataFrame rows into dictionaries/lists for random choice  
- [x] Saving progress by writing updated CSV files (words-to-learn list)  
- [x] Handling file-not-found with try/except to initialize app state  

### 🛠️ Project / Exercise
**Project Name:** Flashcard App  
**Description:**  
- GUI app to help learn words (French → English).  
- Shows a French word for 3 seconds, then flips to show English translation.  
- User can click ✔️ if they know the word (it’s removed from the list).  
- Progress is saved in a `words_to_learn.csv` file, so next run only shows unknown words.  

**My Code:**  
[Link to my code](./Day31_FlashcardApp/main.py)

### 💡 Challenges I Faced
- [x] Forgetting to cancel previous `.after()` calls → caused overlapping timers  
- [x] `KeyError` when trying to access DataFrame columns incorrectly → fixed with correct keys  
- [x] Ensuring the app loads from `words_to_learn.csv` if it exists, otherwise fallback to `french_words.csv`  

### 🚀 Extensions / Improvements
- [ ] Add multiple languages (English–Spanish, English–Hindi, etc.)  
- [ ] Track learning stats (total learned, total remaining, % progress)  
- [ ] Add option to reset progress (start fresh)  
- [ ] Improve UI: larger fonts, better styling, color themes  

### 📖 Resources
- Course: Day 31 – Capstone Project: Flashcard App  
- Docs: [Tkinter Canvas](https://tkdocs.com/tutorial/canvas.html)  
- Docs: [Pandas DataFrame.to_dict()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html)  
- Article: [The Forgetting Curve & Spaced Repetition](https://www.sciencedirect.com/topics/neuroscience/spacing-effect)

