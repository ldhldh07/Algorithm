from collections import defaultdict

def possible_half(coin_dict, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    
    for coin, coin_count in coin_dict.items():
        for i in range(target, -1, -1):
            for j in range(1, coin_count + 1):
                if i - j * coin < 0: 
                    break
                if dp[i - j * coin] == 1:
                    dp[i] = 1
                    break
    return dp[target]


ans_list = []

for _ in range(3):
    N = int(input())
    coin_dict = defaultdict(int)
    coin_sum = 0
    for _ in range(N):
        coin, coin_count = map(int, input().split())
        coin_dict[coin] = coin_count
        coin_sum += coin * coin_count

    if coin_sum % 2 == 1:
        ans_list.append(0)
    else:
        ans_list.append(possible_half(coin_dict, coin_sum // 2))

print(*ans_list, sep='\n')