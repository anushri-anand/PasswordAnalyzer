# Password Strength Analyzer 

A simple **Python GUI application** that analyzes password strength, assigns a score, and stores results in a **SQLite database**. Built using **Tkinter**, **SQLite3**, and **Regex**.


## Features

* Password strength scoring (0–10 scale)
* GUI built using Tkinter
* Passwords stored in SQLite database
* Summary report of password scores
* Automatic database & table creation


## Technologies Used

* Python 3
* Tkinter (GUI)
* SQLite3 (Database)
* Regex (Password validation)

## Password Scoring Criteria

| Criteria                   | Points |
| -------------------------- | ------ |
| Length ≥ 8                 | +2     |
| Length ≥ 12                | +2     |
| Contains numbers           | +2     |
| Contains uppercase letters | +2     |
| Contains symbols           | +2     |

**Maximum Score: 10**

## Database Information

- Database Name:

```
passwords.db
```

- Table Structure:

```sql
CREATE TABLE passwords (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password TEXT,
    score TEXT
);
```

- Stored Data:
    * Password
    * Score


## How to Run

### 1. Clone or Download Project

```bash
git clone <your-repo-link>
cd password-analyzer
```

Or simply download the `.py` file.


### 2. Run the Application

```bash
python password_analyzer.py
```

## Application UI

The GUI contains:

* Password input field
* **Check Password** button
* **Show Summary** button


## Example Summary Output

```
Score 4: 2 passwords
Score 8: 5 passwords
Score 10: 1 passwords
```


## Project Structure

```
password-analyzer/
│
├── password_analyzer.py
├── passwords.db (created automatically)
└── README.md
```


## Important Note

This project stores passwords in **plain text** for learning purposes only.

In real-world applications:

* Use password hashing
* Use encryption
* Follow security best practices


## Future Improvements

* Add password hashing
* Add strength meter bar
* Export summary to CSV
* Add password suggestions
* Add dark mode UI


## License

This project is for educational purposes.


## Learning Outcomes

This project demonstrates:

* Python GUI development
* SQLite database integration
* Regular expressions
* Function-based programming
* Data storage and retrieval

