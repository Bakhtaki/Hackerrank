import os
# Complete the 'solve' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY x as parameter.
#


class Solution:
    def __init__(self, n):
        self.tree = [0] * (n + 1)

    def update(self, i):
        # Update the tree
        i += 1
        while i < len(self.tree):
            self.tree[i] += 1
            i += i & -i

    def query(self, i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.tree[i]
            i -= i & -i
        return ans


def solve(x):
    """Write your code here."""
    length_x = len(x)   # Length of the array
    mod = 10 ** 9 + 7    # Modulo
    missing = [True] * length_x  # Missing array

    # Create 2 solution object
    tree1 = Solution(length_x)
    tree2 = Solution(length_x)

    # Find the missing numbers
    for i in range(length_x):
        x[i] -= 1
        if x[i] != -1:
            missing[x[i]] = False

    # Find the missing elements
    missing_elements = []
    for i in range(length_x):
        if missing[i]:
            missing_elements.append(i)

    # Sum of missing elements
    missing_sum = 0
    m = len(missing_elements)

    # Find the sum of missing elements
    for i in missing_elements:
        missing_sum += i
        if i < n - 1:
            tree2.update(i + 1)

    fact = [1] * 500010

    # Find the factorial
    for i in range(1, 500010):
        fact[i] = (fact[i - 1] * i) % mod

    # Total Cost
    total_cost = 0
    p = 0
    y = 0

    # Find the total cost
    for i in range(length_x - 1):
        if x[i] != -1:
            if m == 0:
                D1 = tree1.query(x[i])
                tree1.update(x[i])
                cost = (x[i] - D1) * fact[length_x - i - 1]
            else:
                D1 = tree1.query(x[i]) * m
                n_of_smaller = tree2.query(x[i])
                D2 = n_of_smaller * p
                tree1.update(x[i] + 1)
                cost = (x[i] * m - (D1 + D2)) * fact[m-1] * \
                    fact[length_x - i - 1]
                y += m - n_of_smaller
        else:
            if p == 0:
                cost = (missing_sum - y) * fact[m - 1] * \
                    fact[length_x - i - 1]
            else:
                D1 = p * m * (m - 1) // 2
                D2 = y * (m - 1)
                cost = (missing_sum * (m - 1) - (D1 + D2)) * \
                    fact[m - 2] * fact[length_x - i - 1]
            p += 1
        total_cost = (total_cost + cost) % mod
    return (total_cost + fact[m]) % mod


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = solve(a)

    fptr.write(str(result) + '\n')

    fptr.close()
