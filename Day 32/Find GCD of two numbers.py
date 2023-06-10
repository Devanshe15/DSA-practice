if __name__=='__main__':
    num1, num2 = map(int,input('enter the numbers').split())
    ans=1
    for i in range (1, min(num1,num2)+1):
        if num1% i==0 and num2 %i==0:
            ans=i
    print('GCD of two numbers is ',ans)