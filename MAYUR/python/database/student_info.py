import sqlite3

conn = sqlite3.connect('students.db')

c=conn.cursor()


 
c.execute("""CREATE TABLE students (
          id INTEGER PRIMARY KEY,
          name TEXT,
          age INTEGER,
          city TEXT
          )""")
