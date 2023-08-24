import sys

def start_index(num, n):
    if num <= 0:
        return 0
    # if num
    result =  num * (num-1) // 2 + 1 if num > 0 else 0

si = sys.stdin.readline

N = int(si().strip())

# 대각선 기준으로 오름차순 배열을 만들때 그 시작점의 index

print(start_index(1))
print(start_index(2))
print(start_index(3))
print(start_index(4))