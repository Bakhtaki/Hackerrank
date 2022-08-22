import os

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    """Write your code here."""
    k = k % 26
    s = list(s)
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
                s[i] = chr((ord(s[i]) - 65 + k) % 26 + 65)
            else:
                s[i] = chr((ord(s[i]) - 97 + k) % 26 + 97)
    return ''.join(s)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

