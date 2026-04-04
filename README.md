# student-data-filtering
A simple Python tool for filtering student records based on major and CGPA with user input.
A Python-based command-line interface (CLI) application designed to search and filter student records efficiently. This project demonstrates core programming concepts like list comprehensions, data structures, and user input handling.


 Features

Filter by Major: Search for students in specific departments (e.g., CS, IT, DS).

Filter by Minimum CGPA: View all students who meet or exceed a specific academic threshold.

Formatted Output: Displays results with the total count and rounded CGPA values.

Error Handling: Prevents crashes by validating numerical inputs for CGPA.

--How It Works
The program uses a list of dictionaries to store student information, including their name, major, and CGPA . It runs in a continuous loop, providing a menu for the user until they choose to exit.


Choose an option from the menu:
1: Filter by Major.
2: Filter by Minimum CGPA.
3: Exit the program.


 Sample Output
==Filter Menu ===
1. Filter by Major | 2. Filter by Min CGPA | 3. Exit
Enter choice (1-3): 1
Enter Major: ds
Major = DS (2 Found)
Name: Diana, Major: DS, CGPA: 7.9
Name: Riya, Major: DS, CGPA: 8.0
