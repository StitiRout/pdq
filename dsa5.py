# print factors
# for eg 10=[1,2,5,10]
# using brute force
a=int(input("Enter a number : "))
result=[]
def factors(a):
   for i in range(1,a+1):
      if a%i==0:
        result.append(i)
   print(result)
   return result
factors(a)      
    
# tc=n
# optimal solution

# a=int(input("Enter a number : "))
# result=[]
# def factors(a):
#    for i in range(1,a//2):
#        if a%i==0:
#         result.append(i)
#    result.append(a)
#    print(result)
#    return result
# factors(a)