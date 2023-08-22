import sys

def prime_divisors(num):
    visited = [0 for _ in range(int(num**0.5)+1)]
    divisors_dict = {}
    for i in range(2, int(num**0.5)+1):
        if visited[i]:
            continue
        while not num % i:
            divisors_dict[i] = divisors_dict.get(i, 0) + 1
            num //= i
        ci = i
        while ci <= int(num**0.5):
            visited[ci] = 1
            ci += i

    if num > 2:
        divisors_dict[num] = divisors_dict.get(num, 0) + 1

    return divisors_dict

si = sys.stdin.readline

N = int(si().strip())

divisors_dict = prime_divisors(N)

answer = 1
for num, square in divisors_dict.items():
    answer *= num ** square - num ** (square-1)

print(answer)