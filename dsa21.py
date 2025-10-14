# Quick sort
arr = [4,1,7,6,3,2,8]
def partition(arr,low,high):
    pivot=arr[low]
    i=low
    j=high
    while i<j:
        while arr[i]<=pivot and i<=high-1:
            i+=1
        while arr[j]>=pivot and j>=low+1:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    arr[low],arr[j]=arr[j],arr[low]
    return j
def quick(arr,low,high):
    if low<high:
        index=partition(arr,low,high)
        quick(arr,low,index-1)
        quick(arr,index+1,high)   
quick(arr,0,len(arr)-1) 
print(arr)
# tc=n square
# sc=1