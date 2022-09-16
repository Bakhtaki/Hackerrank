
import os


#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    # Write your code here
    count = 0

    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            for k in range(j + 1, len(s) - i + 1):
                if sorted(s[j:j+i]) == sorted(s[k:k+i]):
                    count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
