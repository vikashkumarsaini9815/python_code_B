salery=int(input(" enter anual salery :- "))
if salery>0 and salery<250000:
    print("no tax ")
elif salery>=250000 and salery <=500000:
    a=(salery/100)*5
    b=a-12500
    print("5 % ",b)
elif salery>=500000 and salery <=750000:
    a=(salery/100)*10
    b=a-50000+12500
    print(b)
