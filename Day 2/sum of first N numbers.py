def sums(n):
    if n<=0:
        return 0
    else:
        return n+sums(n-1)
