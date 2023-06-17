def checkprime(n):
    for i in range (1,n+1):
        if n%i==0:
            return ('it is not a prime no.')
        else:
            print( n, 'is prime')
n= int(input('enter a no'))
checkprime(n)