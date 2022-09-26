"""Hackerrank Solution for Gridland Province."""
import os

#
# Complete the 'gridlandProvinces' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#
prime = 10000000007 * 65535

prime_map = [int((1 << (5 * i)) % prime) for i in range(1202)]


def c_hash(s, p=0):
    for c in s:
        p = ((p << 5) + ord(c)) % prime
        return p


def hmap(s):
    ret = [0]

    for c in s:
        ret.append(((ret[-1] << 5) + ord(c)) % prime)
    return ret


def hrange(l, i, j, s):
    return (l[j] + ((s - l[i]) * prime_map[j - i])) % prime


def my_custom_count(s1: str, s2: str, s1_rev, s2_rev):
    ret = set()
    n, n2 = len(s1), 2 * len(s1)

    left_to_top = s2_rev + s1
    left_to_bottom = s1_rev + s2
    right_from_top = s1 + s2_rev
    right_from_bottom = s2 + s1_rev

    mid_even_tb = [ord(s1[i // 2]) if ((i % 4) in (0, 3)) else
                   ord(s2[i // 2]) for i in range(n2)]

    mid_odd_tb = [ord(s2[i // 2]) if ((i % 4) in (0, 3)) else
                  ord(s1[i // 2]) for i in range(n2)]

    left_to_top, left_to_bottom, right_from_bottom, right_from_top = \
        map(hmap, (left_to_top, left_to_bottom, right_from_bottom,
                   right_from_top))

    mid_even_tb = [mid_even_tb[2 * j + 1] +
                   mid_even_tb[2 * j] *
                   prime_map[1] for j in range(n)]

    mid_odd_tb = [mid_odd_tb[2 * j + 1] +
                  mid_odd_tb[2 * j] *
                  prime_map[1] for j in range(n)]

    for left, mids, rights in ((left_to_top, (mid_even_tb, mid_odd_tb),
                               (right_from_top,
                                right_from_bottom)),
                               (left_to_bottom, (mid_odd_tb, mid_even_tb),
                                (right_from_bottom, right_from_top))):

        for i in range(0, n + 1):
            mid = mids[i & 1]
            s = hrange(left, n - i, n + i, 0)
            for j in range(i, n):
                ret.add(hrange(rights[j & 1], j, n2 - j, s))
                s = (s * prime_map[2] + mid[j]) % prime
            ret.add(s)
            rights = rights[::-1]
    return ret


def gridlandProvinces(s1, s2):
    """Write your code here."""
    s1_rev, s2_rev = s1[::-1], s2[::-1]

    return len(my_custom_count(s1, s2, s1_rev, s2_rev).union
               (my_custom_count(s1_rev, s2_rev, s1, s2)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input().strip())

    for p_itr in range(p):
        n = int(input().strip())

        s1 = input()

        s2 = input()

        result = gridlandProvinces(s1, s2)

        fptr.write(str(result) + '\n')

    fptr.close()
