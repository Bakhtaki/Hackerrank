#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
        # Write your code here
        temp = arr[-1]
        index = n - 2
        while index >= 0 and arr[index] > temp:
            arr[index + 1] = arr[index]
            print(*arr)
            index -= 1
        arr[index + 1] = temp
        print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

