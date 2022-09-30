T = int(input())

for t in range(1, 1+T):
    N = int(input())
    arr = [0] * 1000

    for n in range(N):

        bus_type, A, B = map(int, input().split())
        arr[A] = arr[B] = 1
        
        if bus_type == 1:
            for i in range(A+2, B-1, 2):
                arr[i] += 1

        elif bus_type == 2:
            for i in range(A+2, B-1, 2):
                arr[i] += 1

        else:
            if A % 2:
                for i in range(A+1,B):
                    if i % 3 == 0 and i % 10 != 0:
                        arr[i] += 1
            else:
                for i in range(A+1,B):
                    if i % 4 == 0:
                        arr[i] += 1
    max_num = 0
    for m in arr:
        if max_num < m :
            max_num = m

    print('#{} {}'.format(t, max_num))
