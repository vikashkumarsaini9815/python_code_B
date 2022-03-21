list1=[1,2,8,9,6]
list2=[3,4,5,6,2,1]
list3=[]
for i in list1:
    for v in list2:
        if i==v:
            list3.append(i)
        else:
            pass
print(list3)        
