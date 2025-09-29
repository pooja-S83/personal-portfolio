<h1>TASK 1</h1>
<h3>Enhanced CLI Calculator 🧮</h3>
<br>
A small, safe, and user-friendly command-line calculator written in Python.
<br>
<b>Features</b>
Basic operations: add, subtract, multiply, divide
Extras: power, square root, percent
Free-form expressions (safe AST-based evaluation)
ans token → reuse last result
Shows and saves calculation history
<br>
<b>Follow the menu options:<b/>
1-7 → basic operations
<br>
8 → enter an expression (2+3*4, ans/2, etc.)
<br>
9 → show history
<br>
S → save history to file
<br>
Q → quit

<h1> TASK2 </h1>
<h3>Weekly To-Do List Manager</h3>

A simple <b>console-based Python application</b> to manage your weekly to-do tasks.  
You can add multiple tasks per day, mark them as done, edit, remove, or clear all tasks at once. Tasks are stored persistently in a text file (`tasks.txt`) in the same folder.

<h5>Features</h5>
- Add tasks for each day of the week (Monday → Sunday)  
- View tasks day-wise with status symbols:
  - ⏳ Pending  
  - 👍 Done  
- Mark a single task as done  
- Edit a task  
- Remove a single task  
- Remove all tasks at once
- Mark all tasks as done 
- Tasks are saved in `tasks.txt` in the same folder, so they persist across sessions

  Follow the on-screen menu to:
1. View tasks
2. Add tasks
3. Mark tasks as done
4. Remove tasks
5. Edit tasks
6. Remove all tasks
7. Mark all tasks as done
8. Exit

<h5>File Structure</h5>
<br>
task2/
│
<br>
├─ todo.py        # Main Python script
<br>
├─ tasks.txt      # Stores your weekly tasks (auto-created)
<br>
└─ README.md      # Project documentation

<h1> TASK3 </h1>
<h3>Web Scraper for News Headlines</h3>

📌 Objective

Build a Python script that automatically scrapes top news headlines from a public website and saves them into a text file.

<h5>🛠 Tools & Libraries Used </h5>
Python 3
<br>
requests – to send HTTP requests and fetch HTML
<br>
BeautifulSoup4– to parse and extract data from HTML
<br>
<b>Project Structure</b>
<br>
├── scraper.py      <br>
├── headlines.txt <br>
<br>

<h5>🚀 How It Works</h5>
<br>
The script sends an HTTP GET request to a news website (e.g., BBC News).
<br>
The HTML response is parsed using BeautifulSoup.
<br>
The program extracts all h2 tags (commonly used for headlines).
<br>
The cleaned text is saved in headlines.txt.
<br>

<h1>task 4</h1>
<h3>REST API with Flask</h3>
<br>
"A simple Flask REST API for managing users with GET, POST, PUT, and DELETE endpoints"
<br>
<h5>🚀 Features</h5>
<br>
- GET all users
<br>
- GET a single user by ID
<br>
- POST new user
<br>
- PUT update user
<br>
- DELETE user
<br>
<br>
<h5>🧠 Notes</h5>
<br>
- All responses are in JSON format.
<br>
- Error messages are descriptive and follow HTTP status codes.
<br>
- Designed for easy extension into database-backed APIs.
<br>

<h1>task 5</h1>
<h3>📊 Sales Data Analysis & Visualization</h3>
<br>
This project demonstrates how to load, process, and visualize sales data using Python's **Pandas** and **Matplotlib** libraries. It includes robust error handling for missing files and provides insights into total sales by product category.
<br>

<h5>🚀 Features</h5>
<br>
- Loads sales data from a CSV file using `pandas.read_csv()`
<br>
- Automatically generates sample data if the CSV is missing
<br>
- Displays DataFrame structure and summary
<br>
- Groups sales by product category using `groupby()` and `sum()`
<br>
- Visualizes results with a clean bar chart using `matplotlib.pyplot`
<br>
- Highlights highest and lowest selling categories
<br>

<h5>📈 Sample Output</h5>
- A bar chart showing total sales by product category
<br>
- Console output summarizing
<br>
- DataFrame structure
<br>
- Total sales per category
<br>
- Highest and lowest selling categories
<br>


<br>
<img width="1000" height="600" alt="task5" src="https://github.com/user-attachments/assets/00cbd935-ecec-4004-99d1-93e7f4b6d483" />


