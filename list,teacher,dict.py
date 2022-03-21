# yha hame list or dict add karke data ko stord karna hai

teacher1={'name':'vicky','subject':'math','time':1.00,'phone':12345}
teacher2={'name':'ravi','subject':'hindi','time':2.00,'phone':56789}
teacher3={'name':'akhil','subject':'portical','time':3.00,'phone':9876}
teacher4={'name':'gopal','subject':'chemistry','time':4.00,'phone':54321}
teacher_list=[teacher1,teacher2,teacher3,teacher4]
teacher_mobail=int(input("name find karne ke liye phone number put kare  "))
for teacher in teacher_list:
    if teacher["phone"]==teacher_mobail:
        print(teacher["name"])

