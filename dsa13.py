# Reverse an array using recursion
# using for loop 
def reverse_subarray(arr,left,right):
    for i in range((right-left+1)//2):
        arr[left+i] , arr[right-i] = arr[right-i],arr[left+i]
    return arr
arr=[1,2,3,4,5,6,7,8,9,0]
left=2
right=5
print("Given array is : ",arr)
print("Reverse sunarray is  : ",reverse_subarray(arr,left,right))