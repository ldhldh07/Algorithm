A, B = map(int, input().split())

counting_tree = [0 for _ in range(B+1)]
counting_tree[1] = 1
counting_sum = [0 for _ in range(B+1)]
for num in range(2, B+1):
    counting_tree[num] = counting_tree[num // 2] + (1 if num % 2 else 0)
    counting_sum[num] = counting_sum[num-1] + counting_tree[num]

