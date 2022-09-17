
import os
from collections import Counter
#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#


def steadyGene(gene):
    """Write your code here."""
    n = len(gene)
    gene_map = Counter(gene)

    extra = ""
    for key, val in gene_map.items():
        if val > n//4:
            extra += key*(val-n//4)
    m = len(extra)
    if m == 0:
        return 0

    extra_map = Counter(extra)
    i, j, count, ans, temp_map = 0, 0, 0, n, {}

    def add_to_temp(count):
        temp_map[gene[j]] = temp_map.get(gene[j], 0) + 1
        if temp_map.get(gene[j]) <= extra_map.get(gene[j], 0):
            count += 1
        return temp_map, count, j+1

    while j < n:
        if count < m:
            temp_map, count, j = add_to_temp(count)
        else:
            ans = min(ans, j-i)
            if temp_map.get(gene[i], 0)-1 >= extra_map.get(gene[i], -1):
                temp_map[gene[i]] -= 1
                i += 1
            else:
                temp_map, count, j = add_to_temp(count)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()
