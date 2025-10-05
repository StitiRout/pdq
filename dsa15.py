# String palindrome
a=input("Enter a string : ")
def palinndrome():
    n=len(a)
    Left=0
    Right=n-1
    while Left<Right:
        if a[Left]!=a[Right]:
            print("not")
            return
        Left+=1
        Right-=1
    print("yes")
palinndrome()


