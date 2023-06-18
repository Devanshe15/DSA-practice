class Solution:    
    #Complete this function
    def printNos(self,N,i=1):
        #Your code here
        if i==N:
            print(N,end=" ")
        else:
            print(i,end=" ")
            i=i+1
            self.printNos(N,i)
