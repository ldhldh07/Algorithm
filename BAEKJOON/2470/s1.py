N = int(input())
solutions = list(map(int, input().split()))
solutions.sort()

start = 0
end = N-1
min_sum_mix = abs(solutions[end] + solutions[start])
answer = (start, end)
while start < end:
    sum_mix = solutions[start] + solutions[end]

    if abs(sum_mix) < min_sum_mix:
        min_sum_mix = abs(sum_mix)
        answer = (start, end)

    if sum_mix < 0:
        start += 1
    else:
        end -= 1


print(solutions[answer[0]], solutions[answer[1]])