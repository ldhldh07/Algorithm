import sys

def multiply_matrix(matrix_a, matrix_b, size):
    arr = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for w in range(size):
                arr[i][j] += (matrix_a[i][w] * matrix_b[w][j]) % 10 ** 9
                arr[i][j] %= 10 ** 9
    return arr

def square_matrix(matrix, size):
    return multiply_matrix(matrix, matrix, size)


def fibonacci(n):
    n -= 1
    base = [[1, 1], [1, 0]] 
    result = [[1, 0], [0, 1]]
    while n:
        if n % 2:
            result = multiply_matrix(result, base, 2)
        base = square_matrix(base, 2)
        n //= 2
    return result[0][0]


def fibonacci_sum(n):
    return fibonacci(n+2) - 1


si = sys.stdin.readline

a, b = map(int, si().strip().split())
answer = 0

print((fibonacci_sum(b)-fibonacci_sum(a-1)+ 10 ** 9) % 10 ** 9)
