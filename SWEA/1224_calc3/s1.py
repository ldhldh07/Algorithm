T = 10

isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

for t in range(1, T+1):

    N = int(input())
    calc = input()
    stack = [0] * N
    top = -1
    formula = ''

    for c in calc:

        if c not in ['*', '/', '+', '-', '(', ')']:  # 토큰이 피연산자일때
            formula += c                             # 출력할 값에 더해줍니다

        elif c == '(':                               # 여는 괄호일 때 스택에 넣어줍니다.
            top += 1
            stack[top] = c

        elif c == ')':                               # 닫는 괄호일 때는 여는 괄호 나올때까지 pop, 출력해줍니다
            while stack[top] != '(':
                formula += stack[top]
                stack[top] = 0
                top -= 1
            stack.pop()                              # 여는괄호는 pop해줍니다
            top -= 1

        elif icp[c] > isp[stack[top]]:               # 입력된 토큰의 우선순위가 stack[top]의 우선순위보다 높을때
            top += 1                                 # 토큰을 스택에 넣어줍니다
            stack[top] = c

        else:                                        # 우선순위가 낮을 때는
            while icp[c] <= isp[stack[top]]:         # 높아질 때까지
                formula += stack[top]                # pop해주면서 출력한 값에 더해줍니다
                stack[top] = 0
                top -= 1
                if top == -1:
                    break
            top += 1                                 # 우선순위가 높아지거나 스택에 값이 없게 되면
            stack[top] = c                           # 토큰을 스택에 넣어줍니다

    while top >= 0:                                  # 스택에 남은 값들을 top에서부터 formula에 더해줍니다
            formula += stack[top]
            top -= 1
                                                     # formula 변수의 값이 후위계산법 문자열입니다

    stack2 = [0] * N
    top = -1
    result = 0

    for f in formula:                         # 나온 식으로 계산을 합니다

        if f == '*':
            top -= 1                          # *일 경우 stack[top]와 stack[top-1] 팝하고 더해서 stack[top]에 넣어줍니다
            stack[top] = int(stack[top]) * int(stack[top+1])
            stack[top+1] = 0

        elif f == '+':                        # +일 경우도 마찬가지로 해줍니다
            top -= 1
            stack[top] = int(stack[top]) + int(stack[top+1])
            stack[top+1] = 0

        elif f == '/':                        # /일 경우도 마찬가지로 해줍니다
            top -= 1
            stack[top] = int(int(stack[top]) / int(stack[top+1]))
            stack[top+1] = 0

        elif f == '-':                        # -일 경우도 마찬가지로 해줍니다
            top -= 1
            stack[top] = int(stack[top]) - int(stack[top+1])
            stack[top+1] = 0

        else:
            top += 1                           # 피연산자일 경우 스택에 더해줍니다
            stack[top] = int(f)


    print('#{} {}'.format(t, stack[0]))        # 마지막에 남은 값을 출력해줍니다