class Solution:
    def nextPermutation(self, n, arr):
        pivot = n-1
        while(pivot>=0 and arr[pivot]<=arr[pivot-1]):
            pivot-=1
        # print(pivot)
        j = n-1
        while(j>pivot-1 and arr[j]<=arr[pivot-1]):
            j-=1
        # print(j)
        arr[pivot-1],arr[j] = arr[j],arr[pivot-1]
        
        arr[pivot:] = sorted(arr[pivot:]) 
        return arr