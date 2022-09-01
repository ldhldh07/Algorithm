N = int(input())
for a in range(5):
    if N - 3 * a >= 0 and (N - 3 * a) % 5 == 0:
        print((N - 3 * a)//5 + a)
        break
else:
    print(-1)