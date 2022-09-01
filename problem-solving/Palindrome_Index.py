import os
#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def palindromecheck(s, i, j):
    """Write Your Code Here."""
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def palindromeIndex(s):
    """Write your code here."""
    i, j = 0, len(s) - 1
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1

    # String Already is Palindrome
    if i >= j:
        return -1
    # if remove left one makes string Palindrome
    if palindromecheck(s, i + 1, j):
        return i
    # if remove right one makes string palindrome
    if palindromecheck(s, i, j - 1):
        return j
    # impossible make string palindrome
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
