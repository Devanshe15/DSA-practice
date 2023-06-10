if __name__ == '__main__':
    N = int(input('enter the number'))
    reverse = 0
    while N != 0:
        #digit stores the remainder that is last digit
        digit = N % 10
        reverse = reverse * 10 + digit
        #now N is the first two digits
        N = N // 10
    print(reverse)