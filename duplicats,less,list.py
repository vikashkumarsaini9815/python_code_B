list1=[10,"hi",20,30,10,30,"vicky","hi"]
list2=[]
for ele in list1:
    if ele not in list2:
        list2.append(ele)
print("duplicat free list :- ", list2)
