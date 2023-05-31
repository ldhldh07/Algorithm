def make_triangle(top_i, top_j):
    arr[top_i][top_j] = '*'
    arr[top_i+1][top_j-1] = '*'
    arr[top_i+1][top_j+1] = '*'
    arr[top_i+2][top_j-2] = '*'
    arr[top_i+2][top_j-1] = '*'
    arr[top_i+2][top_j] = '*'
    arr[top_i+2][top_j+1] = '*'
    arr[top_i+2][top_j+2] = '*'

N = int(input())

for n in range(11):
    if N == 3 *2**n:
        k = n
        break

width = 5
top_j = 2
for a in range(k):
    top_j = width
    width = width * 2 + 1

top_list = [(0, top_j)]
for nn in range(k):
    new_top_list = []
    for top_i, top_j in top_list:
        new_top_list.append((top_i+3*2**nn, top_j-3*2**nn))
        new_top_list.append((top_i+3*2**nn, top_j+3*2**nn))
    top_list.extend(new_top_list)

arr = [[' ' for _ in range(width)] for _ in range(N)]

for top_i, top_j in top_list:
    make_triangle(top_i,top_j)

for line in arr:
    print(''.join(line))
