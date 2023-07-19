N = int(input())
solutions = list(map(int, input().split()))

start, end = 0, N-1
min_value = 2 * 10 ** 9

answer = (0, 0)
while start < end:
    mix_solution = solutions[start] + solutions[end]
    
    if abs(mix_solution) < min_value:
        min_value = abs(mix_solution)
        answer = (solutions[start], solutions[end])

    if mix_solution < 0:
        start += 1
    else:
        end -= 1

print(*answer)