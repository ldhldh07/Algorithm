import sys
from collections import defaultdict

def prime_factorization(n):
    visited = [0 for _ in range(int(n**0.5)+1)]
    num_dict = defaultdict(int)

    for i in range(2, int(n**0.5)+1):
        if visited[i]:
            continue
        while not n % i:
            num_dict[i] += 1
            n //= i
        if n == 1:
            break
        for j in range(i, int(n**0.5)+1, i):
            visited[j] = 1

    if n > 1:
        num_dict[n] += 1

    return num_dict


def euler_phi(n):
    answer = 1
    dd = prime_factorization(n)

    for a, b in dd.items():
        answer *= (a**b) - (a**(b-1))

    return answer


def get_divisors(n):
    divisors = []

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: 
                divisors.append(n // i)

    return sorted(divisors)


si = sys.stdin.readline

n = int(si().strip())

divs = get_divisors(n)

answer = -1

for x in divs:
    if x * euler_phi(x) == n:
        answer = x
        break

print(answer)