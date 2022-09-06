import sys
sys.setrecursionlimit(10 ** 6)                            # 재귀호출시 런타임에러 방지

def dfs(i,j):                                             # 델타탐색하면서 빈공간을 2로 바꾸는 함수 선언
    global ans                                            # 글로벌 함수로 ans 가져와서 크기 구하기
    if arr[i][j] == 0:                                    # 비어있을 경우
        arr[i][j] = 2                                     # 2로 채워주고
        ans += 1                                          # ans += 1 해주어서 2로 바뀐 갯수만큼 크기로 만들어줍니다
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:        # 델타 탐색
            ni, nj = i + di, j + dj                       # 이동하면서 시점 변경
            dfs(ni, nj)                                   # 변경한 곳에서 dfs 재귀호출
        else:                                             # for문을 다 돌았을 경우 즉, 연결되는 칸들을 다 2로 바꾼 후
            return ans                                    # ans를 반환

M, N, K = map(int, input().split())
arr = [[1] * (N+2)] + [[1] + [0] * (N) + [1] for _ in range(M)] + [[1] * (N+2)]  # 벽을 1로 하는 2차원 배열 생성
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())            # 두 모서리 좌표 입력받음
    for i in range(M-y2+1,M-y1+1):                        # y좌표는 위로 커지고 i는 아래로 커지는 모양새기 때문에 M기준 빼줌
        for j in range(x1+1, x2+1):                       # x는 같은 방향이며 칸인거 감안하고 벽 감안해서 계산
            arr[i][j] = 1                                 # 색칠된 칸은 1로 바꿔줌

ans_list = []                                             # 답이 들어갈 리스트
len_ans = 0                                               # 답 갯수
for i in range(1, M+1):                                   # 벽 제외한 2차열 배열 탐색
    for j in range(1, N+1):
        ans = 0                                           # 0일경우 앞서 선언한 연결된 0 다 2로 바꿔주면서 크기 재는 함수 돌림
        dfs(i, j)
        if ans:                                           # 답이 0이 아닐 경우
            len_ans +=1                                   # 답 갯수 더해주고
            ans_list.append(ans)                          # 답은 리스트에 넣어줌

ans_list.sort()                                           # 오름차순 정렬
print(len_ans)
print(" ".join(map(str, ans_list)))
    