import sys

arr = list(sys.stdin.readline().strip())
arr2 = []
N = int(input())

for _ in range(N):
    key_in = sys.stdin.readline().strip().split()
    if key_in[0] == 'L' and arr:
        arr2.append(arr.pop())
    elif key_in[0] == 'D' and arr2:
        arr.append(arr2.pop())
    elif key_in[0] == 'B' and arr:
        arr.pop()
    elif key_in[0] == 'P':
        arr.append(key_in[1])

sys.stdout.write(''.join(arr) + ''.join(reversed(arr2)))
