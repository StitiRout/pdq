# Recursion using parameters
# print a b times
# eg def fxn(a,b)

def fxn(a,b):
    if b==0:
        return 
    print(a)
    fxn(a,b-1)
fxn(15,4)

# print i to N using recursion

def fxn2(c,d):
    if c>d:
        return
    print(c)
    fxn2(c+1,d)
fxn2(1,10)

# print N to i

def fxn3(n):
    if n==0:
        return
    print(n)
    fxn3(n-1)
fxn3(10)