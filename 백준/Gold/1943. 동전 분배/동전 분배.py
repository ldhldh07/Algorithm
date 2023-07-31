from collections import defaultdict

def possible_half(coin_dict, target):
    available_moneys = set([0])

    for coin, coin_count in sorted(coin_dict.items(), reverse=True):
        new_moneys = set()
        for available_money in available_moneys:
            for i in range(1, coin_count + 1):
                next_available_money = available_money + coin * i
                if next_available_money > target:
                    break
                new_moneys.add(next_available_money)
                if next_available_money == target:
                    return 1
        available_moneys.update(new_moneys)
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