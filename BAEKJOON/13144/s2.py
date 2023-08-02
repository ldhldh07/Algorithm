N = int(input())
num_list = list(map(int, input().split()))

num_dict = {}
start_index = 0
ans = 0

for index, num in enumerate(num_list):
    if num in num_dict and start_index <= num_dict[num]:
        start_index = num_dict[num] + 1
    num_dict[num] = index
    ans += index - start_index + 1
    print(index - start_index + 1)

print(ans)