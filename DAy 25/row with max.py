class Solution:

    def rowWithMax1s(self,arr, n, m):
        max=0
        val=-1
        for i in range(n):
            c=0
            s=0
            e=m-1
            while(s<=e):
                mid=(s+e)//2
                if arr[i][mid]==1:
                    e=mid-1
                    c=m-mid
                elif arr[i][mid]<1:
                    s=mid+1
                else:
                    e=mid-1
            
            if c>max:
                max=c
                val=i
                
        return val
                