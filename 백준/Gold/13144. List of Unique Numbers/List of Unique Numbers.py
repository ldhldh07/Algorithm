N = int(input())
num_list = list(map(int, input().split()))

num_dict = {}
ans = 0
start_unique = 0

for index, num in enumerate(num_list):
    if num in num_dict and num_dict[num] >= start_unique:
        start_unique = num_dict[num] + 1
    num_dict[num] = index
    ans += index - start_unique + 1

print(ans)