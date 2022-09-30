T = int(input())

for t in range(1, T+1):
    formula = input().split()
    stack = [0] * 256
    top = -1

    for f in formula:

        if f in ['*', '/', '+', '-'] and top < 1:                   # 스택에 숫자 2개 미만일 때 기호가 입력되면
            print('#{} error'.format(t))                            # 에러가 납니다
            break

        elif f == '*':
            top -= 1                                                # *일 경우 stack[top]와 stack[top-1] 팝하고 더해서 stack[top]에 넣어줍니다
            stack[top] = int(stack[top]) * int(stack[top + 1])
            stack[top + 1] = 0

        elif f == '+':                                              # +일 경우도 마찬가지로 해줍니다
            top -= 1
            stack[top] = int(stack[top]) + int(stack[top + 1])
            stack[top + 1] = 0

        elif f == '/':                                              # /일 경우도 마찬가지로 해줍니다
            top -= 1
            stack[top] = int(int(stack[top]) / int(stack[top + 1]))
            stack[top + 1] = 0

        elif f == '-':                                              # -일 경우도 마찬가지로 해줍니다
            top -= 1
            stack[top] = int(stack[top]) - int(stack[top + 1])
            stack[top + 1] = 0

        elif f == '.':                                              # .이 나올 경우
            print('#{}'.format(t), end=' ')
            if top != 0:                                            # 스택에 숫자가 2개 이상 있으면 에러
                print('error')
            else:                                                   # 한개만 남아있을 경우
                print(stack[0])                                     # 마지막에 남은 값을 출력해줍니다

        else:
            top += 1                                                # 피연산자일 경우 스택에 더해줍니다
            stack[top] = int(f)