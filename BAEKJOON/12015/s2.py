import bisect

N = int(input())
A = list(map(int, input().split()))

LIS = [A[0]]

for i in range(1, N):
    if A[i] > LIS[-1]:  # 현재 원소가 리스트의 마지막 원소보다 크면 리스트에 추가
        LIS.append(A[i])
    else:  # 그렇지 않으면 리스트에서 현재 원소보다 큰 원소 중 가장 작은 것의 위치를 찾아서 그 위치에 현재 원소를 넣음
        LIS[bisect.bisect_left(LIS, A[i])] = A[i]

print(len(LIS))
