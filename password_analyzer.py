import sqlite3
import re

import tkinter as tk
from tkinter import messagebox

# Function to check password strength

def check_score(password):
    score = 0

    # Check Length
    if len(password) >= 8:
        score += 2
    if len(password) >= 12:
        score += 2

    # Check Numbers
    if re.search(r"\d", password):
        score += 2

    # Check uppercase
    if re.search(r"[A-Z]", password):
        score += 2

    # Check symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2

    # Maximum score
    return score

# Save password to database

def save_to_db(password, score):
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    # Create table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS passwords
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  password TEXT,
                  score TEXT)''')
    # Insert password
    c.execute("INSERT INTO passwords (password, score) VALUES (?, ?)", (password, score))
    conn.commit()
    conn.close()

# Check password button

def check_password():
    pwd = password_entry.get()
    if not pwd:
        messagebox.showwarning("Warning", "Please enter a password!")
        return
    
    score = check_score(pwd)
    save_to_db(pwd,score)
    messagebox.showinfo("Password Score", f"Password Score: {score}/10")
    password_entry.delete(0,tk.END)

# Show summary button 

def show_summary():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT score, COUNT(*) FROM passwords GROUP BY score")
    results = c.fetchall()
    conn.close()

    summary_text = "\n".join([f"Score {row[0]}: {row[1]} passwords" for row in results])
    if not summary_text:
        summary_text = "No passwords stored yet."
    messagebox.showinfo("Password Score Summary", summary_text)

# Tkinter GUI

root = tk.Tk()
root.title("Password Strength Analyzer")

tk.Label(root,text="Enter Password: ").pack(pady=5)
password_entry = tk.Entry(root,show="*",width=30)
password_entry.pack(pady=5)

tk.Button(root,text = "Check Password", command=check_password).pack(pady=5)
tk.Button(root,text="Show Summary", command=show_summary).pack(pady=5)

root.geometry("300x180")
root.mainloop()