N = int(input())

heights = list(map(int, input().split()))

asc_stack = []
answer = [[0, 10**5+1, -1] for _ in range(N)]

for index in range(N):
    if asc_stack:
        while asc_stack and heights[asc_stack[-1]] <= heights[index]:
            asc_stack.pop()
        answer[index][0] += len(asc_stack)
        answer[index][1] = min(answer[index][1], index - asc_stack[-1])
        answer[index][2] = asc_stack[-1][index]
    asc_stack.append(index)

desc_stack = []

for index in range(N-1, -1, -1):
    if desc_stack:
        while desc_stack and heights[desc_stack[-1]] <= heights[index]:
            desc_stack.pop()
        answer[index][0] += len(desc_stack)
        if answer[index][1] > desc_stack[-1] - index:
            answer[index][1] = desc_stack[-1] - index
            answer[index][2] = asc_stack[-1][index]
    desc_stack.append(index)

for ans in answer:
    if not ans[0]:
        print(0)
    else:
        print(*ans)