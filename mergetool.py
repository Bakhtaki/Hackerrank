"""Merge string Tools."""

def merge_the_tools(string, k):
    """Merge string Tools."""
    for i in range(0, len(string), k):
        temp = string[i:i+k]
        print(''.join(j for i, j in enumerate(temp) if j not in temp[:i]))

        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
