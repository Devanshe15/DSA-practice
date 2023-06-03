def binarysearch(list, low, high ,x):
    while low <= high:
        mid = low +(high-low)//2
        if list [mid]==x:
            return mid
        elif list[mid]<x:
            low= mid-1 
        else:
            high=mid+1
    return -1
list = [2,3,4,5,6,7,6,6]
x = 3
result = binarysearch(list,0, len(list)-1,x)
if result != -1:
    print ("element is present at index",result)
else:
    print("element is not present in the list")