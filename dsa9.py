# Recursion
# Tail recursion first recursion then job
c=0
def fxn2():
    global c
    if c==4:
        return
    c+=1
    fxn2()
    print("A")
fxn2()