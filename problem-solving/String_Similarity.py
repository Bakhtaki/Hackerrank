import os

#
# Complete the 'stringSimilarity' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def stringSimilarity(s):
    # Write your code here
    len_s = len(s)
    z = [0] * len_s

    zbox_left, zbox_right, z[0] = 0, 0, len_s

    for i in range(1, len_s):
        if i < zbox_right:
            k = i - zbox_left
            if z[k] < zbox_right - i:
                z[i] = z[k]
                continue
            zbox_left = i
        else:
            zbox_left = zbox_right = i
        while zbox_right < len_s and\
                s[zbox_right - zbox_left] == s[zbox_right]:
            zbox_right += 1
        z[i] = zbox_right - zbox_left

    return sum(z)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()
