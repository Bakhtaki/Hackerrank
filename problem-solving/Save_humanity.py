#!/bin/python3
#
# Complete the 'virusIndices' function below.
#
# The function accepts following parameters:
#  1. STRING p
#  2. STRING v
#


def small_match(w1, w2):
    counter = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            counter += 1
            if counter > 1:
                return 0
    return 1


def match(w1, w2):
    length = len(w1)
    if length < 10:
        return small_match(w1, w2)
    w11 = w1[:length // 2]
    w12 = w1[length // 2:]
    w21 = w2[:length // 2]
    w22 = w2[length // 2:]

    s1 = (w11 == w21)
    s2 = (w12 == w22)

    if s1 and s2:
        return True
    elif s1 and not s2:
        return match(w12, w22)
    elif not s1 and s2:
        return match(w11, w21)
    else:
        return False


def virusIndices(p, v):

    res = ''
    if len(v) > len(p):
        return "No Match!"
    else:
        for i in range(len(p) - len(v) + 1):
            temp = p[i:i + len(v)]

            flag = match(temp, v)
            if flag:
                res += str(i) + ' '
        if len(res) == 0:
            return "No Match!"
        else:
            return res.strip()


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        p = first_multiple_input[0]

        v = first_multiple_input[1]

        print(virusIndices(p, v))
