# merge sort
arr=[3,1,2,4,1,5,2,6,4]
def divide(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    l_arr=arr[:mid]
    r_arr=arr[mid:]
    l=divide(l_arr)
    r=divide(r_arr)
    return merge(l,r)
def merge(l,r):
    result=[]
    i=0
    j=0
    n=len(l)
    m=len(r)
    while i<n and j<m:
        if l[i] <= r[j]:
            result.append(l[i])
            i+=1
        else:
            result.append(r[j])
            j+=1
    
    while i<n:
            result.append(l[i])
            i+=1
    
    while j<m:
            result.append(r[j])
            j+=1
    return result

print(divide(arr))
