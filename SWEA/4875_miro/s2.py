# 4875_미로 풀이
# 2022-08-23

T = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

for t in range(1, T+1):
    N = int(input())                                         # 기존 리스트에 1로 상하좌우 벽 쳐서 2차원 배열 만들어줍니다
    arr = [[1] * (N+2)] + [[1]+list(map(int,input()))+[1] for _ in range(N)] + [[1] * (N+2)]
    stack = [0] * N * N                                      # 각 위치별로 이동했던 방향을 함수로 만들어줍니다
    top = -1

    top += 1                                                 # 시작점을 push해줍니다
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 2:
                stack[top] = (i, j)

    result = 0                                               # 기본값은 0으로 둡니다
    print(arr)
    while True :
        vi = stack[top][0]
        vj = stack[top][1]
        for i in range(4):

            if arr[vi+di[i]][vj+dj[i]] == 3:             # i방향으로 이동했을 때 3이면
                print(stack)
                for a in arr:
                    print(a)
                result = 1                               # 결과 1로 하고 break
                break
            elif arr[vi+di[i]][vj+dj[i]] != 0:           # 1 혹은 2면 pass합니다
                arr[vi+di[i]][vj+dj[i]] = 1
                print(stack)
                for a in arr:
                    print(a)
                pass
            else:                                        # 0이면 그쪽으로 이동합니다
                vi, vj = vi+di[i], vj+dj[i]
                arr[vi][vj] = 1                          # 이동한 곳 1로 바꿔줍니다
                top += 1                                 # stack에 push 해줍니다
                stack[top] = (vi, vj)
                print(stack)
                for a in arr:
                    print(a)
                break
        else:                                                # break되지 않았으면, 즉 4방향 막혀있으면
            stack[top] = 0                                   # pop해주면서 왔던 길 되돌아갑니다
            top -= 1

        if top == -1:                                        # 이때 스택에 원소가 없으면 길이 없다는 뜻이므로 break해줍니다
            break                                            # 이 경우 초기값인 0이 그대로 출력됩니다

    print('#{} {}'.format(t, result))