import math
import os
import random
import re
import sys


def cookies(k, A):
    A = sorted(A, reverse = True)
    count = 0
    temp = []
    l = 0
    while A and A[-1] < k or temp and temp[l] < k:
        if len(A) + len(temp[l:l+2]) < 2:
            count = -1
            break            
        else:
            count += 1
            a0 = []
            for num, i in enumerate(range(min(2, len(A)))): 
                a0.append((A[-num-1], 0))
            a1 = []
            tmp = temp[l:l+2]
            for num, i in enumerate(range(min(2, len(tmp)))): 
                a1.append((tmp[num], 1))
            b = sorted(a0+a1, key=lambda x: x[0])[:2]
            for i in range(2):
                if b[i][1] == 0:
                    A.pop()
                else:
                    l += 1
            temp.append(b[0][0] + b[1][0]*2)            
    return count