import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def get_candidate(gcd):
    result = [gcd]
    for n in range(2, int(gcd ** 0.5) + 1):
        if gcd % n == 0:
            result.append(n)
            if n **2 != gcd:
                result.append(gcd // n)
    return sorted(result)

si = sys.stdin.readline

N = int(si().strip())
nums = [int(si().strip()) for _ in range(N)]

differences = [abs(nums[i] - nums[i-1]) for i in range(1, N)]
diff_gcd = differences[0]
for i in range(1, N-1):
    diff_gcd = gcd(differences[i], diff_gcd)

answer = get_candidate(diff_gcd)

print(*answer, sep=" ")