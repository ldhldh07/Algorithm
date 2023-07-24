N = int(input())
solutions = sorted(list(map(int, input().split())))

min_abs_sum = 3 * 10 ** 9

for start in range(N-2):
    middle, end = start + 1, N-1
    start_solution = solutions[start]

    while middle < end:
        mix_solution = start_solution + solutions[middle] + solutions[end]
        
        if abs(mix_solution) < min_abs_sum:
            min_abs_sum = abs(mix_solution)
            answer = [start, middle, end]
        
        if mix_solution > 0:
            end -= 1
        else:
            middle += 1

print(*[solutions[index] for index in answer])