# we have to load students data here
student1={'name':'kalu','class':'1st year','phone':12345,'12th':'60.00'}
student2={'name':'shankar','class':'2nd year','phone':6789,'12th':'50'}
student3={'name':'parkash','class':'final year','phone':54321,'12th':'78.89'}
student4={'name':'shree ram','class':'berozgar','phone':9876,'12th':'39.83'}
student_list=[student1,student2,student3,student4]
stu_12th=input("enter 12th %   " )
for student in student_list:
    if student['12th']==stu_12th: 
        print(student['class'])
