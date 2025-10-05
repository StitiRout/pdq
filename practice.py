# Strore frequency practice
a=input("Enter a num : ")
hash_map={}

for i in range(len(a)):
    if a[i] in hash_map:
        hash_map[a[i]]+=1
    else:
        hash_map[a[i]]=1
print(hash_map)


num=input("Enter numbers")
length=len(num)
freq_map={}
for i in range(0,length):
    freq_map[num[i]]=freq_map.get(num[i,0])+1
print(freq_map)


list1=[9,0,7,8,3,4,5,7,7,8]
list2=[0,1,2,3,4,5,6,7,8,9]
list3=[0]*11
for i in list1:
    list3[i]=1
for j in list2:
    if j<0 and j>10:
        print(0)
    else:
        print(list3[i])
print(list3)