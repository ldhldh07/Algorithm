in_stack_precedence = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

in_coming_precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '(': 3,
}


formula = list(input())
stack = []
for token in formula:
    # 숫자 나오면 일단 출력
    if token not in ['+', '-', '*', '/', '(', ')']:
        print(token, end='')
        continue
    # 여는 괄호 만나거나 아무것도 없을때면
    elif token == '(':
        stack.append(token)
    # 여는 괄호 만나면
    elif token == ')':
        # 여는 괄호 나올때까지 출력후
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        # 여는 괄호는 출력 안하고 pop해버림
        if stack:
            stack.pop()
        # print(stack)
        # print(token)
    else:
        while stack and in_stack_precedence.get(stack[-1], 0) >= in_coming_precedence.get(token, 0):
            # top에 있는 값을 체크해서 지금 넣는 값의 우선순위 보다 높으면 출력한다
            print(stack.pop(), end='')
            # 낮은 값이 나오면 그때 token을 append한다
        stack.append(token)
while stack:
    print(stack.pop(), end='')
