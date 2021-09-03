from typing import Counter


def Sum(L, i, n, count):

    if n <= i:
        return count
    
    count+=L[i]

    count = Sum(L, i+1,n,count)

    return count

L = [1,2,3,4,5]
count = 0
n = len(L)
print(Sum(L,0,n,count))