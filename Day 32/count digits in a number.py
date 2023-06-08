def countdigit(n):
    count=0
    x=n
    while (x!=0):
        x=x//10
        count += 1
    return count
n = int(input('enter the digit'))
print(countdigit(n))