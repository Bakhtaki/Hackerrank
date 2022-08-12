#!/bin/python3

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def almostSorted(arr):
    """ Write your code here."""
    # Scenario 1: Check if arr is sorted, if not got to Scenario 2
    sort_arr = sorted(arr)
    if arr == sort_arr:
        print('yes')
    # Scenario 2 or 3: Swap or Reverse
    else:
        # get the difference of sorted_arr - arr
        difference = [x-y for x, y in zip(arr, sort_arr)]
        # Scenario 2: Swap
        # when number of 0 in difference == 2, then swap is probably suitable.
        if len(arr) - 2 == difference.count(0):
            index_1, index_2 = [index for index, x in enumerate(
                difference) if x != 0]  # get the index to swap
            # swap the value
            arr[index_1], arr[index_2] = arr[index_2], arr[index_1]
            if arr == sort_arr:  # if swapped_arr = sorted_arr then yes.
                print('yes')
                print(f'swap {index_1 +1} {index_2 +1}')
            else:
                return 'no'
        # Scenario 3: Reverse
        else:
            # get those index that point to the value > 0 in 'difference'
            index_of_great_than_0 = [index for index,
                                     x in enumerate(difference) if x != 0]
            star, end = min(index_of_great_than_0), max(
                index_of_great_than_0)  # find the start and end index of subset
            # reverse the subset of arr and use append everything to form a new list
            reserved_arr = arr[:star] + \
                list(reversed(arr[star:end+1])) + arr[end+1:]
            if reserved_arr == sort_arr:
                print('yes')
                print(f'reverse {star + 1} {end+1}')
            else:
                print('no')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
