def divisor(n):
    for i in range (1,n+1):
        if n%i==0:
            print(i)
        else:
            continue
num= int(input())
divisor(num)
