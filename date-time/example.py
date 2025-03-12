import sqlite3

# Connect to the database (or create one if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create a table with an auto-incrementing primary key
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")

# Insert user data (ID will be assigned automatically)
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
cursor.execute("INSERT INTO users (name) VALUES (?)", ("Bob",))

# Commit changes and close connection
conn.commit()
conn.close()
