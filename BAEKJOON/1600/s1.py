def dfs(x, y):
    for move in [[2, 1], [2, -1], [-2, 1], [-2, -1]]:
        nx, ny = x + move[0], y + move[1]
        if not arr[nx][ny]:
            dfs(nx, ny)


K = int(input())

W, H = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(H)]


print(arr)

'''
말처럼 이동하는거나 원숭이처럼 이동하는거나 다 스택에 넣어서 DFS로 풀어버리기
다만 이미 방문한 곳은 그 때까지 횟수를 저장한 후 그 곳까지 가는 횟수가 더 크면 멈춰!
'''
start_point = (1,1)

