class Solution:
    def rearrange(self,arr, n):
        pos = []
        neg = []
        for val in arr:
            if val < 0:
                neg.append(val)
            else:
                pos.append(val)
        if len(pos) > len(neg):
            x = len(neg)
            y = neg
            z = pos
            a = x*2
        else:
            x = len(pos)
            y = pos
            z = neg
            a = x*2
        for i in range(0,x):
            arr[i*2] = pos[i]
            arr[ (i*2) + 1 ] = neg[i]
        
        for j in range(x,len(z)):
            arr[a] = z[j]
            a+=1