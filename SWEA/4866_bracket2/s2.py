# 4866_괄호검사 풀이
# 2022-08-18

T = int(input())

for t in range(1, T + 1):

    word = input()
    bracket = ''
    b_cnt = 0

    for a in word:                                                 # 괄호있는것만 따로 분류합니다.
        if a in ['(', ')', '{', '}']:
            bracket += a
            b_cnt += 1

    size = b_cnt
    stack = [0] * size
    top = -1
    bracket_dict = {')':'(', '}':'{'}

    for b in bracket:                                               # 입력받은 값들 반복문
        if b == '(' or b == '{':                                    # '(','{'일 경우 push
            top += 1
            stack[top] = b
        elif b in bracket_dict and stack[top] == bracket_dict[b]:   # ')','}'일경우 stack[top]이 호응될 때
            top -= 1                                                # pop
        else:                                                       # 위의 경우 아닌 모든 경우에 오류이므로
            ans = 0                                                 # ans = -1 로 break
            break
    else:                                                           # break 되지 않고 끝까지 반복마친다면
        if top == -1:                                               # 스택에 원소가 없으면(top이 바닥이면)
            ans = 1                                                 # ans = 1
        else:                                                       # 원소가 남아있으면
            ans = 0                                                 # ans = -1

    print('#{} {}'.format(t, ans))