import sys

def get_divisors_count(num, n):
    count = 0
    for a in range(1, int(num**0.5)+1):
        # print(a)
        if not num % a:
            if num // a <= n:
                count += 1
                if not a ** 2  == num:
                    count += 1
    return count

si = sys.stdin.readline

# N = int(si().strip())

prefix_sum = 0
# for num in range(min(10**9, N*2)):

print(get_divisors_count(9, 6))