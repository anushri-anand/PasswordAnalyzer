import sqlite3
import re

# Function to check password strength

def check_strength(password):
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
                  strength TEXT)''')
    # Insert password
    c.execute("INSERT INTO passwords (password, strength) VALUES (?, ?)", (password, score))
    conn.commit()
    conn.close()

# Function to show summary

def show_summary():
    conn = sqlite3.connect("passwords.db")
    c = conn.cursor()
    c.execute("SELECT strength, COUNT(*) FROM passwords GROUP BY strength")
    results = c.fetchall()
    print("\n--- Password Strength Summary ---")
    for row in results:
        print(f"Score {row[0]}: {row[1]} passwords")
    conn.close()

# Main program

def main():
    print("=== Password Strength Analyzer ===")
    while True:
        password = input("\nEnter a password (or type 'quit' to exit): ")
        if password.lower() == "quit":
            break
        score = check_strength(password)
        print(f"Password Score: {score}/10")
        save_to_db(password, score)

    show_summary()
    print("\nAll passwords have been saved to passwords.db")

if __name__ == "__main__":
    main()