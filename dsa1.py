# Extraction of digit in reverse order
# a=int(input("Enter a number :" ))
# while a >0:
#     result=a%10
#     print(result)
#     a=a//10

# count the digits
a=int(input("Enter a number :" ))
count=0
while a >0:
    count+=1
    a=a//10
print( count)