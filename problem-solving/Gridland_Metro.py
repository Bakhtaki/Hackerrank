import os

#
# Complete the 'gridlandMetro' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER k
#  4. 2D_INTEGER_ARRAY track
#


def gridlandMetro(n, m, k, track):
    # Write your code here
    dict = {}
    total = n * m

    for i in range(k):
        row = track[i][0]
        start = track[i][1]
        end = track[i][2]

        # Row not in dict
        if row not in dict:
            dict[row] = [start, end]
        # if row in dict and not overlapping
        elif start > dict[row][1]:
            total -= end - start + 1
        # if row in dict and overlapping
        elif end > dict[row][1]:
            dict[row][1] = end

    tracks = 0
    for key in dict:
        tracks += dict[key][1] - dict[key][0] + 1

    return total - tracks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    track = []

    for _ in range(k):
        track.append(list(map(int, input().rstrip().split())))

    result = gridlandMetro(n, m, k, track)

    fptr.write(str(result) + '\n')

    fptr.close()
