T = int(input())

for t in range(T):
    A, B, C, D = map(int, input().split())

    for num in range(-10**6, 10**6+1):
        if not A * num ** 3 + B * num ** 2 + C * num + D:
            alpha = num
            break

    a = A
    b = A * alpha + B
    c = b * alpha + C
    
    if b ** 2 - 4 * a * c >= 0:
        beta = (- b + (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
        gamma =  (- b - (b ** 2 - 4 * a * c) ** (1/2)) / (2 * a)
        ans = set([alpha, beta, gamma])
    else:
        ans = [alpha]
    
    print(*sorted(ans))