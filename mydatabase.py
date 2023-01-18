import sqlite3
con=sqlite3.connect('mydatabase.db')
cursorobj=con.cursor()
cursorobj.execute("insert into student1 values("Saravanan", "software engineer", "CSE","kuzhitrhura")")
con.commit()
con.close()