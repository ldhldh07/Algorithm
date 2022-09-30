T = 10

for t in range(1, 1+T):
    N, arr = input().split()
    N = int(N)
    stack = [0] * N                  # 사이즈는 N인 스택을 만듭니다
    top = -1

    for num in arr:                  # arr 문자열 반복문으로 돌려줍니다.
        if stack[top] == num:        # 맨 위에 같은 값이 있다면 붙어있다는 것이기에
            top -= 1                 # pop해주며 이는 글자에서 붙어있는 두개 제거해주는 단계와 같습니다.
        else:
            top += 1                 # 아닐경우 스택에 쌓아줍니다.
            stack[top] = num
    print('#{}'.format(t), end=' ')
    for b in range(top+1):
        print(stack[b], end='')
    print()
