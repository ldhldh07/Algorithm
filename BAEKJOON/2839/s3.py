N = int(input())
for a in range(5):
    M = N - 3 * a
    if M >= 0 and M % 5 == 0:
        print(M//5 + a)
        break
else:
    print(-1)