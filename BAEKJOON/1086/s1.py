import sys, math

si = sys.stdin.readline

N = int(si().strip())
nums = [int(si().strip()) for _ in range(N)]
K = int(si().strip())
# i번째 줄의 j번째 10**i*j번째 수 곱한것에 나머지
remainders = [[((prev_remainder * 10**len(str(num))) % K + num) % K for prev_remainder in range(K)] for num in nums]

print(remainders)

'''
(기존숫자 * 10**len(새로운숫자) + 새로운 숫자) % K
(기존숫자 * 10**len(새로운 숫자)) % K + 새로운 숫자 % K
(기존숫자 % K) * 10**len(새로운숫자) % K + 새로운 숫자 % K = 다 합쳐진 숫자 % K
dp[mask][remainder] += dp[mask ^ (1<<u)][prev_reminder]
(prev_remainder * 10**len(nums[u]) + nums[u]) % k = remainder

'''

# 마스크대로 숫자를 넣었을 때 K가 나머지인 갯수
dp = [[0 for _ in range(K)] for _ in range(1 << N)]
# 0000일때 나머지 0인 경우는 1
dp[0][0] = 1
for mask in range(1<<N):
    for current_num in range(N):
        # 지금 순번의 숫자가 아직 안들어간 경우
        if not mask & (1 << current_num):
            for remainder in range(K):
                # 지금 순번에서 u만큼 더한 dp의 나머지에 더해준다?
                dp[mask | (1 << current_num)][remainders[current_num][remainder]] += dp[mask][remainder]

zero_case = dp[(1<<N)-1][0]
total_case = sum(dp[(1<<N)-1])

div = math.gcd(zero_case, total_case)

print("{}/{}".format(zero_case // div, total_case // div))
