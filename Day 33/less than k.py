def lessthan(lst,k):
    result = []
    for num in lst:
        if num < k:
            result.append(num)
    return result
lst=[1,-2,0,5,-3]
k=4
print(lessthan(lst,k))