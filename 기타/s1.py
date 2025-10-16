def can_balance(weights, target):
    total_sum = sum(weights)  # 추들의 총합을 계산
    
    # 목표는 (target + total_sum)의 절반을 만들 수 있는지 확인하는 것
    if (total_sum + target) % 2 != 0:
        return False
    
    target_sum = (total_sum + target) // 2
    
    # 부분합 문제를 풀기 위한 DP 테이블
    dp = [False] * (target_sum + 1)
    dp[0] = True  # 부분합이 0인 경우는 항상 가능
    
    # 추들로 부분합을 만들 수 있는지 확인
    for weight in weights:
        for i in range(target_sum, weight - 1, -1):
            dp[i] = dp[i] or dp[i - weight]
    
    return dp[target_sum]

# 테스트
print(can_balance([1, 1, 5, 9], 7))  # True
print(can_balance([2, 5, 8, 9], 12)) # True
print(can_balance([1, 4, 10], 8))    # False
