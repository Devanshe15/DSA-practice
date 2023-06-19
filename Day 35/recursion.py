 def printNos(self,N,i=1):
    if i==N:
        print(N,end=" ")
    else:
        print(i,end=" ")
        i=i+1
        self.printNos(N,i)
