import sqlite3

conn = sqlite3.connect('students.db')

c=conn.cursor()


 
# c.execute("""CREATE TABLE students (
#           name TEXT,
#           age INTEGER,
#           class TEXT,
#           no TEXT
#           )""")
# c.execute("INSERT INTO students VALUES ('prince jagani',25,'c',6352549555)")     

# all_students = [
#     ('coetzee',25,'d',523626544),
#     ('david',23,'b',8523697410),
#     ('omrazai',27,'a',6398452595),
#     ('mayur',25,'b',6365452315) 
      
# ]



# c.executemany("INSERT INTO students VALUES (?,?,?,?)",all_students )    



c.execute("SELECT * FROM students")

print(c.fetchall())



items=c.fetchall()
# for item in items:
#     print(item)
    

# c.execute("""UPDATE students SET name = 'prince'
#           WHERE rowid=1
          
          
#           """)

c.execute("""DELETE from students 
          WHERE id=6
          
          
          """)
    
conn.commit()   
conn.close()  
