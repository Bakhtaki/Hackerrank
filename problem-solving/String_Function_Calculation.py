#!/bin/python3
from operator import le
import os


#
# Complete the 'maxValue' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING t as parameter.
#

def maxValue(t):
    n = len(t)
    sa = suffix_array(t, n)
    lcp = lcp_array(t, sa, n)
    ans = n
    left, right = [-1]*n, [n]*n
    s = [0]
    for i in range(1, n):
        while s and lcp[s[-1]] >= lcp[i]:
            s.pop()
        if s:
            left[i] = s[-1]
        s.append(i)
    s = [n-1]
    for i in range(n-2, -1, -1):
        while s and lcp[s[-1]] >= lcp[i]:
            s.pop()
        if s:
            right[i] = s[-1]
        s.append(i)
    for i in range(n):
        ans = max(ans, lcp[i]*(right[i]-left[i]))
    return ans


def suffix_array(s, n):
    sa, l = [[s[i], i] for i in range(n)], 0
    while l < 2*n:
        sa.sort(key=lambda x: x[0])
        last, rank, pos_map = sa[0][0], 0, [None]*n
        for i in range(n):
            pos_map[sa[i][1]] = i
            if last != sa[i][0]:
                last = sa[i][0]
                rank += 1
            sa[i][0] = rank
        new_tuple = [(sa[i][0], sa[pos_map[sa[i][1]+l]][0]
                      if sa[i][1]+l < n else -1) for i in range(n)]
        for i in range(n):
            sa[i][0] = new_tuple[i]
        l = 1 if not l else l << 1
    return [i[1] for i in sa]


def lcp_array(s, sa, n):
    rank, k, lcp = [None]*n, 0, [0]*n
    for i in range(n):
        rank[sa[i]] = i
    for i in range(n):
        if rank[i] == n-1:
            k = 0
            continue
        j = sa[rank[i]+1]
        while i+k < n and j+k < n and s[i+k] == s[j+k]:
            k += 1
        lcp[rank[i]] = k
        k = max(0, k-1)
    return lcp


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = input()

    result = maxValue(t)

    fptr.write(str(result) + '\n')

    fptr.close()
