num=int(input("enter number :- " ))
for i in range (2,num):
    if num%i==0:
        print("not prime :- ",num)
        break
else :
    print(" number is prime :- " ,num)
