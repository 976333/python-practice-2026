import sqlite3

# Sample data
data = [
    {"name": "Alice", "age": 30, "role": "Engineer"},
    {"name": "Bob", "age": 25, "role": "Designer"},
    {"name": "Charlie", "age": 35, "role": "Manager"}
]

# 1. Connect to database and create the table structure
conn = sqlite3.connect("company.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        role TEXT
    )
""")

# 2. Prepare the SQL statement with placeholders
query = "INSERT INTO employees (name, age, role) VALUES (:name, :age, :role)"

# 3. Execute bulk insert safely using executemany
cursor.executemany(query, data)

conn.commit()
conn.close()
