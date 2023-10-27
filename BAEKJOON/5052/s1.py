import sys

si = sys.stdin.readline

t = int(si().strip())
ans_list=[]
for _ in range(t):
    n = int(si().strip())
    nums = []
    for _ in range(n):
        word = si().strip()
        nums.append(word)
    nums.sort()
    for i in range(len(nums)-1):
        fw = nums[i]
        sw = nums[i+1]

        if sw[:len(fw)] == fw:
            ans_list.append("NO")
            break
    else:
        ans_list.append("YES")

print(*ans_list, sep='\n')