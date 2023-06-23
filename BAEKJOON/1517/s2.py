class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0 for _ in range(size+1)]
    
    def update(self, value):
        while value <= self.size:
            print(value)
            self.tree[value] += 1
            # 이진법의 가장 마지막 1을 더해주면서 업데이트
            value += value & -value 
    
    def query(self, i):
        cumulative_sum = 0
        while i > 0:
            cumulative_sum += self.tree[i]
            # 이진법의 가장 마지막 1의 값들을 더해줌
            i -= i & -i
        return cumulative_sum

N = int(input()) 
arr = list(map(int, input().split()))

temp = sorted(list(set(arr)))
rank = {temp[i]: i+1 for i in range(len(temp))}

fenwick_tree = FenwickTree(len(temp))

ans = 0
for i, num in enumerate(arr):
    if i > 0:
        ans += i - fenwick_tree.query(rank[num])
    fenwick_tree.update(rank[num])

print(ans)