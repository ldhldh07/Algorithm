N = int(input())

heights = list(map(int, input().split()))

asc_stack = []
answer = [[0, -1, -1] for _ in range(N)]

for index in range(N):
    while asc_stack and heights[asc_stack[-1]] <= heights[index]:
        asc_stack.pop()

    if asc_stack:
        answer[index][0] += len(asc_stack)
        if answer[index][1] == -1 or index - asc_stack[-1] < answer[index][1]:
            answer[index][1] = index - asc_stack[-1]
            answer[index][2] = asc_stack[-1] + 1
            
    asc_stack.append(index)

desc_stack = []

for index in range(N-1, -1, -1):
    while desc_stack and heights[desc_stack[-1]] <= heights[index]:
        desc_stack.pop()
        
    if desc_stack:
        answer[index][0] += len(desc_stack)
        if answer[index][1] == -1 or desc_stack[-1] - index < answer[index][1]:
            answer[index][1] = desc_stack[-1] - index
            answer[index][2] = desc_stack[-1] + 1
            
    desc_stack.append(index)

for ans in answer:
    if ans[0] == 0:
        print(0)
    else:
        print(ans[0], ans[2])
