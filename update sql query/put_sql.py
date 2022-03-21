userid = "4"
username = "kartik"
emails = "kartik@444gmail.com"
mobile = "90876543"
password = "jjjjkkk.848"
rpassword = "jhfjk0.845"

sql = "UPDATE reg SET user ={}, email = {},mob = {},pass = {},rpass = {} WHERE id={} ".format(userid,username,emails,mobile,password,rpassword,)
print(sql)

# convert tuple to dict
  
def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
      
# Driver Code    
tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))
    
