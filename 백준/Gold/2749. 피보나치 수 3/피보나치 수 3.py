def multiply_matrix(first_matrix, second_matrix, n):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for index in range(n):
                result[i][j] += (first_matrix[i][index] * second_matrix[index][j]) % 1000000
    return result


def square_matrix(matrix, n):
    return multiply_matrix(matrix, matrix, n)


N = int(input())

base_matrix = [[1, 1], [1, 0]]
ans = [[1, 0], [0, 1]]

N -= 1
while N:
    if N % 2:
        ans = multiply_matrix(ans, base_matrix, 2)
    base_matrix = square_matrix(base_matrix, 2)
    N = N // 2

print(ans[0][0] % 1000000)