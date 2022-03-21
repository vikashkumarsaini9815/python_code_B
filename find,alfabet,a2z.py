# count number of characters a to z 
str1="bbbbbbfhfhfjdjdueueueiwiwkaaaaaeieieowpowpqwlakamzmxnxnbcbcn"
for i in range (97,123):
    count=0
    for v in str1:
        if chr(i)==v:     
            count=count+1
    print("counting of character :- ",chr(i),count)
        
