# Bubble sort

def bubble(a):
    num=len(a)
    for i in range(num-2,-1,-1):
        for j in range(0,i+1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=[1,8,2,4,0,5] 
print(bubble(a))           