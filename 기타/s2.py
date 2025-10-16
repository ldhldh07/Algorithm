def can_balance_knapsack(Weights, Target):
    total_sum = sum(Weights)
    
    # 저울의 한쪽이 Target, 다른 한쪽이 추들로 만들어지는 무게가 목표
    if total_sum < Target:
        return False

    target_sum = (total_sum - Target) // 2
    
    if (total_sum - Target) % 2 != 0:
        return False
    
    dp = [False] * (target_sum + 1)
    dp[0] = True
    
    for weight in Weights:
        for i in range(target_sum, weight - 1, -1):
            if dp[i - weight]:
                dp[i] = True

    return dp[target_sum]

# 예제 테스트
print(can_balance_knapsack([1, 1, 5, 9], 7))  # True
print(can_balance_knapsack([2, 5, 8, 9], 12)) # True
print(can_balance_knapsack([1, 4, 10], 8))    # False
