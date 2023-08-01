from collections import defaultdict

def possible_half(coin_dict, target):
    available_moneys = set([0])
    for coin, coin_count in coin_dict.items():
        temp = available_moneys.copy()
        for available_money in temp:
            for i in range(1, coin_count+1):
                next_available_money = available_money + coin * i
                if next_available_money == target:
                    return 1
                if next_available_money <= target:
                    available_moneys.add(next_available_money)
    return 0

ans_list = []

for _ in range(3):
    N = int(input())
    coin_dict = defaultdict(int)
    coin_sum = 0
    for _ in range(N):
        coin, coin_count = map(int, input().split())
        coin_dict[coin] = coin_count
        coin_sum += coin * coin_count

    if coin_sum % 2 == 0:
        ans_list.append(possible_half(coin_dict, coin_sum // 2))
    else:
        ans_list.append(0)

print(*ans_list, sep='\n')
