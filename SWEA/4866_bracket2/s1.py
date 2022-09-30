T = int(input())

for t in range(1, T+1):

    stack = [0] * 1000
    top = -1

    word = input()
    bracket = ''
    for a in word:
        if a in ['(',')','{','}']:
            bracket += a

    match_dict = {')': '(', '}': '{'}

    for b in bracket:                         # 입력받은 값들 반복문
        if b in match_dict.values():                          # '('일 경우 push
            top += 1
            stack[top] = b
        elif b in match_dict:
            if stack[top] == match_dict[b]:   # ')'이고 top이 '('일 때 pop
                top -= 1
            else:                                # 스택에 '('가 없을 때 ')'가 입력되면
                ans = -1                          # ans = -1 로 break
                break
    else :                                    # break 되지 않고 끝까지 반복마친다면
        if top == -1:                         # 스택에 원소가 없으면(top이 바닥이면)
            ans = 1                           # ans = 1
        else :                                # 원소가 남아있으면
            ans = 0                           # ans = -1

    print('#{} {}'.format(t, ans))
