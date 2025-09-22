# Reverse of an subarray from an array using Reursion

def reverse_subarray(arr,l,r):
    if l>=r:
        return
    arr[l],arr[r]=arr[r],arr[l]
    reverse_subarray(arr,l+1,r-1)
def reverse(arr,left,right):
    reverse_subarray(arr,left,right)
    return arr
arr = [1, 2, 3, 4, 5, 6, 7]
print("Original:", arr)
print("After reversing subarray (2 to 5):", reverse(arr, 2, 5))