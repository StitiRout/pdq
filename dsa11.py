# Functional Recursion
# sum of 1 to n

def fxn(sum,a,b):
    if a>b:
        print(sum)
        return
    fxn(sum+a,a+1,b)
fxn(0,1,10)