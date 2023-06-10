def armstrongno(n):
    count=0
    orginalno=n
    temp=n
    while temp!=0:
        count+=1
        temp =temp// 10
    sumofpower =0
    while n!=0:
        digit =n%10
        sumofpower += pow(digit,count)
        n=n//10
    return sumofpower == orginalno
if __name__=='__main__':
    num= int(input('enter the number'))
    if armstrongno(num):
        print('Yes, it is an Armstrong Number')
    else:
        print('No, it is not an Armstrong Number')    

     


