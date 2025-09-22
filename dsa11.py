
# sum of 1 to n

# def fxn(sum,a,b):
#     if a>b:
#         print(sum)
#         return
#     fxn(sum+a,a+1,b)
# fxn(0,1,10)

#Functional Recursion
# F(N)=N+F(N-1)
def fxn2(n):
    if n==1:
        return 1
    return n+fxn2(n-1)
print(fxn2(10))
