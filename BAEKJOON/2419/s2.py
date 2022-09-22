a = int(input())
arr = list(map(int,input().split()))
cnt = 1
ans = [1]
for i in range(1, a):
    if arr[i-1] <= arr[i]:
        cnt += 1
    elif arr[i-1] > arr[i]:
        ans.append(cnt)
        cnt = 1
    if i == a-1:
        ans.append(cnt)
        cnt = 1
for j in range(a-1, 0, -1):
    if arr[j-1] >= arr[j]:
        cnt += 1
    elif arr[j-1] < arr[j]:
        ans.append(cnt)
        cnt = 1
    if j == 1:
        ans.append(cnt)
        cnt = 1
print(max(ans))