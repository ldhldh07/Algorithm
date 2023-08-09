N, a, b = map(int, input().split())

# 추가된 부분: a와 b의 합이 N+1보다 큰 경우는 불가능하므로 -1 출력
if a + b > N + 1:
    print(-1)
    exit()

heights = [1 for _ in range(N)]

# 단비가 볼 수 있는 건물의 높이 설정
current_index = N - 1
for building_i in range(b):
    heights[current_index] = N - building_i
    current_index -= 1

# 가희가 볼 수 있는 건물의 높이 설정
remaining_height = N - b - 1  # 가장 높은 높이부터 시작
for building_j in range(a - 1):
    if current_index < 0:
        break
    heights[current_index] = remaining_height
    remaining_height -= 1
    current_index -= 1

# 출력
for index in range(N):
    if index != N-1:
        print(heights[index], end=" ")
    else:
        print(heights[index])
