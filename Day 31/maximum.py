def MaximizeEqualNumbers (n, k, a):
    maxCount=0
    for i in range(len(a)):
        num=a[i]
        for X in range(-k,k+1):
            new_num = num+X
            count = a.count (new_num)
            maxCount = max(maxCount, count)
    return maxCount
    pass

T = input()
for i in range(T):
    n, k = map(int, raw_input().split())
    a = map(int, raw_input().split())

    out_ = MaximizeEqualNumbers(n, k, a) 
    
    print (out_)

