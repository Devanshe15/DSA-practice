def reverse(X):
    Y=0
    while(X>0):
        digit= X % 10
        Y= Y*10 +digit
        X= X//10
    return Y

if __name__ == '__main__':
    X= int(input('enter the no'))
    dummy =X
    Y= reverse(X)
    if Y == dummy:
        print('it is palindrome')
    else:
        print('Not palindrome')    
