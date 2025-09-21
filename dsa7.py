# Hashing

# Brute force way
# worst case
list1=[9,0,7,8,3,4,5,7,7,8]
list2=[0,1,2,3,4,5,6,7,8,9]
list3=[]
for i in list2:
    count=0
    for j in list1:
        if j == i:
            count+=1
    list3.append(count)
print(list3)


# Optimal method
# best case
a=[9,0,7,8,3,4,5,7,7,8]
b=[0,1,2,3,4,5,6,7,8,9]
hash_list=[0]*11
for i in a:
    hash_list[i]+=1
for j in b:
       if j<1 or j>10:
          print(0)
       else:
          print(hash_list[i])
print(hash_list)