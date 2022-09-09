

arr = list(input())
N = int(input())
cursor = len(arr)
for _ in range(N):
    key_in = input().split()
    if key_in[0] == 'L' and cursor != 0:
        cursor -= 1
    elif key_in[0] == 'D' and cursor != len(arr):
        cursor += 1
    elif key_in[0] == 'B' and cursor != 0:
        arr.pop(cursor-1)
        cursor -= 1
    elif key_in[0] == 'P':
        arr.insert(cursor, key_in[1])
        cursor += 1

print(''.join(arr))
