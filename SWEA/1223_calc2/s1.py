T = 10

isp = {'*': 2, '/': 2, '+': 1, '-': 1}
icp = {'*': 2, '/': 2, '+': 1, '-': 1}

for t in range(1, T+1):

    N = int(input())
    calc = input()
    stack = [0] * N
    top = -1
    formula = ''

    for c in calc:

        if c not in ['*', '/', '+', '-']:     # 토큰이 피연산자일때
            formula += c                      # 출력할 값에 더해줍니다
                                              # 연산자이면서
        elif top == -1:                       # 스택이 비어있을 때는
            top += 1                          # 입력된 값을 넣어줍니다
            stack[top] = c

        elif icp[c] > isp[stack[top]]:        # 입력된 토큰의 우선순위가 stack[top]의 우선순위보다 높을때
            top += 1                          # 토큰을 스택에 넣어줍니다
            stack[top] = c

        else:                                 # 우선순위가 낮을 때는
            while icp[c] <= isp[stack[top]]:  # 높아질 때까지
                formula += stack[top]         # pop해주면서 출력한 값에 더해줍니다
                stack[top] = 0
                top -= 1
                if top == -1:
                    break
            top += 1                          # 우선순위가 높아지거나 스택에 값이 없게 되면
            stack[top] = c                    # 토큰을 스택에 넣어줍니다

    while top >= 0:                           # 스택에 남은 값들을 top에서부터 출력해줍니다
            formula += stack[top]
            top -= 1

    stack2 = [0] * N
    top = -1
    result = 0

    for f in formula:

        if f not in ['*', '/', '+', '-']:
            top += 1
            stack[top] = int(f)

        elif f == '*':
            top -= 1
            stack[top] = int(stack[top]) * int(stack[top+1])
            stack[top+1] = 0

        elif f == '/':
            top -= 1
            stack[top] = int(stack[top]) / int(stack[top+1])
            stack[top+1] = 0

        elif f == '+':
            top -= 1
            stack[top] = int(stack[top]) + int(stack[top+1])
            stack[top+1] = 0

        else:
            top -= 1
            stack[top] = int(stack[top]) - int(stack[top+1])
            stack[top+1] = 0

    print('#{} {}'.format(t, stack[0]))