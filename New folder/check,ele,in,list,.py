import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vicky1598",
  database="regester"
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM reg")
myresult = mycursor.fetchall()
result = []
#print (myresult)
for row in myresult :
     #   row_dict = {}
        row_dict = {"user":row[0],"email":row[1],"mob":row[2],"pass":row[3],"rpass":row[4]}
      #  row_dict['']=row
        result.append(row_dict)
print(result)


#  python  algorithim
#step 1
#itretion of myresult  as varabal_name row
#result = []
#for row in myresult :
#step 2
#row_dict = {"user":row[0],"email":row[1],"mob":row[2],"pass":row[3],"rpass":row[4]}
#result.append(row_dict)

