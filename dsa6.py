# store frequency in dictionary
# num=[2,2,4,5,6,3,4,5,6,7,8,7,8,9,0]
# how many times the key repeats that will be stored in value's place
# METHOD 1
# a=input("Enter a number : ")
# freq_map={}
# for i in range(len(a)):
#     if a[i] in freq_map:
#         freq_map[a[i]]+=1
#     else:
#         freq_map[a[i]]=1
# print(freq_map)
# TC=N
# SC=N

# METHOD 2
a=input("Enter a number : ")
hash_map={}
n=len(a)
for i in range(0,n):
    hash_map[a[i]]=hash_map.get(a[i],0)+1
print(hash_map)