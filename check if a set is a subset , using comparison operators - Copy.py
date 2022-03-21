import sqlite3

conn=sqlite3.connect(r'C:\Users\pushp\Desktop\database\data1.db')
cur=conn.cursor()
##cur.execute('CREATE TABLE userDetails (fullName, description)')
##names = [description[0] for description in cur.description]
##print(names)
##data=[]
##for i in range(100000):
##        data.append((
##        "vikash"+str(i),
##        "created descrioption"+str(i)
##        
##                ))
##cur.executemany("INSERT INTO userDetails VALUES (?,?)", data)
##conn.commit()
##conn.close()
cur.execute("SELECT * FROM userDetails WHERE fullName = 'vikash9999'")
  
# printing the cursor data
print(cur.fetchall())
##cur = conn.cursor()
##cur.execute("PRAGMA database_list")
##rows = cur.fetchall()
##
##for row in rows:
##    print(row[0], row[1], row[2])
