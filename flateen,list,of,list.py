list1=[1,2,3,[1,2],3,4]
list2=[]
for i in list1:
    if isinstance(i,list):
        for v in i:
            list2.append(i)
         print(list2)

    else :
        list2.append(i)
print(list2)
