class Solution:
    def rearrange(self,arr, n):
        A=[]
        B=[]
        ans=[]
        for i in arr:
            if i<0:
                B.append(i)
            else:
                A.append(i)
        i=0
        j=0
        while i<len(A) or j<len(B):
            if i<len(A):
                ans.append(A[i])
            if j<len(B):
                ans.append(B[j])
            i=i+1
            j=j+1
        for i in range(0,len(arr)):
            arr[i]=ans[i]
        return     
                
                