def factorialNumbers(self, N):
        c=N
        e=1
        d=[]
        for i in range(1,c+1):
            if N>1 and N%i==0 or N//i>0:
                e=e*i
                d.append(e)
                N=N//i
            else:
                break
        return d