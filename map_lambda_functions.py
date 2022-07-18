'''Solution for HackerRank problem "Map Lambda Functions"'''

cube = lambda x: pow(x,3)   # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
        return fib[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
