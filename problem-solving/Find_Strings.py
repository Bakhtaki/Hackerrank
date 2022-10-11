#!/usr/bin/py
# Head ends here
def findStrings(a, query):
    temp = {}
    suffixes = []
    LCP = []
    for s in a:
        for i in range(len(s)):
            val = s[i:]
            if val not in temp:
                temp[val] = 1
                suffixes.append(val)

    suffixes.sort()
    n = len(suffixes)
    for i in range(n):
        if i == 0:
            LCP.append(None)
        else:
            LCP.append(find_lcp(suffixes[i-1], suffixes[i]))

    # num_sub_str = sum(len(s) for s in suffixes) - \
    #     sum(v for v in LCP if v is not None)

    for q in query:
        print(find_ith(suffixes, LCP, q-1))


def find_ith(suffixes, LCP, i):
    data = zip(suffixes, LCP)
    low = high = 0
    for suf, lcp in data:
        if lcp is None:
            lcp = 0
        high += len(suf) - lcp
        if high - 1 == i:
            return suf
        elif high - 1 > i:
            for _i, j in enumerate(list(range(lcp, len(suf)))):
                if low + _i == i:
                    return suf[:j+1]
        low = high
    return "INVALID"


def find_lcp(s1, s2):
    upper_bound = min(len(s1), len(s2))
    count = 0
    for i in range(upper_bound):
        if s1[i] == s2[i]:
            count += 1
        else:
            return count
    return count
# Tail starts here


if __name__ == '__main__':
    n = int(input())
    string = []
    for i in range(0, n):
        string.append(input().strip())
    q = int(input())
    query = []
    for i in range(0, q):
        t1 = int(input())
        query.append(t1)
    findStrings(string, query)
