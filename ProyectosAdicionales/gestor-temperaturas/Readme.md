# 🌡️ Temperature Manager

Python application that allows you to manage a list of temperatures, either by entering them manually or loading them from a file. It includes statistical calculations, detection of cold streaks, and save options.

---

## 📌 Features

- Manual temperature entry with validation.  
- Load temperatures from a file (`temperaturas.txt`).  
- Calculate:
  - Average temperature  
  - Maximum temperature  
  - Minimum temperature  
  - List of negative temperatures  
  - Longest streak of sub-zero temperatures  
- Delete a specific temperature with confirmation.  
- Generate a complete report.  
- Save the current list to a file.  
- Interactive console menu.  

---

## ▶️ How to Run

1. Make sure you have **Python 3.x** installed.  
2. Open a terminal in the project folder.  
3. Run:

```bash
python src/temperaturas.py
```
## 🧪 Example Usage
When starting the program, you will see:

How do you want to load temperatures?

- Enter manually
- Load from file
The main menu allows you to:
1. Delete a temperature  
2. Calculate average temperature  
3. Max/Min temperature  
4. List negative temperatures  
5. Longest sub-zero streak  
6. Generate report  
7. Load list from file (overwrites current list)  
8. Save list and exit  
9. Show current list

## 📄 Notes
The file `temperaturas.txt` should contain one temperature per line.

Menu option 7 overwrites the current list.

The program validates that entered temperatures are real numbers.

## 🛠 Requirements
Python 3.8 or higher
No external libraries required

## 📚 Author
Project developed by Álvaro as part of his personal collection of Python projects.