N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
max_last_line = min_last_line = arr[0]

for i in range(1, N):
    max_temp_line = [0, 0, 0]
    min_temp_line = [0, 0, 0]
    max_temp_line[0] = max(max_last_line[0], max_last_line[1]) + arr[i][0]
    min_temp_line[0] = min(min_last_line[0], min_last_line[1]) + arr[i][0]
    max_temp_line[1] = max(max_last_line[0], max_last_line[1], max_last_line[2]) + arr[i][1]
    min_temp_line[1] = min(min_last_line[0], min_last_line[1], min_last_line[2]) + arr[i][1]
    max_temp_line[2] = max(max_last_line[1], max_last_line[2]) + arr[i][2]
    min_temp_line[2] = min(min_last_line[1], min_last_line[2]) + arr[i][2]

    min_last_line, max_last_line = min_temp_line, max_temp_line     
print(max(max_last_line), min(min_last_line))