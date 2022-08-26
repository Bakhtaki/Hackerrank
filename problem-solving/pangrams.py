import os
#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.


def pangrams(s):
    """Write your code here."""
    s = s.lower()
    len_s = len(list(set(s)))

    if len_s == 27:
        return "pangram"
    return "not pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()

