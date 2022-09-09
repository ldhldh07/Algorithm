from collections import deque
import sys

arr = deque(sys.stdin.readline().strip())  # deque안에 커서 왼쪽 리스트 넣어줍니다
arr2 = deque()                             # 커서 오른쪽 리스트로 빈 deque 만들어줍니다
N = int(sys.stdin.readline().strip())      # 입력받을 횟수입니다

for _ in range(N):
    key_in = sys.stdin.readline().strip().split() # 입력받습니다
    if key_in[0] == 'L' and arr:           # L이면 왼쪽 리스트 하나 오른쪽으로 보냅니다
        arr2.appendleft(arr.pop())
    elif key_in[0] == 'D' and arr2:        # D면 오른쪽 리스트에서 왼쪽 빼서 왼쪽 보냅니다
        arr.append(arr2.popleft())
    elif key_in[0] == 'B' and arr:         # B면 왼쪽 리스트 하나 뺴줍니다
        arr.pop()
    elif key_in[0] == 'P':                 # P면 왼쪽리스트에 값 넣어줍니다
        arr.append(key_in[1])

sys.stdout.write(''.join(arr) + ''.join(arr2))
