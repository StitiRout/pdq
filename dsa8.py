# Recursion 
# Head recursion first job then recuesion
# printing 'A' 4 times
count = 0
def fxn():
    global count
    if count == 4:
        return
    print('A')
    count+=1
    fxn()
fxn()

# Tail recursion first recursion then job
c=0
def fxn2():
    if count==4:
        return
    fxn2()
    print("A")
fxn2()