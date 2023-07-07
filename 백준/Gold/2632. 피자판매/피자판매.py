from collections import defaultdict

def get_sum_dict(pizzas, size, selling_size):
    sum_dict = defaultdict(int)
    if sum(pizzas) <= selling_size:
        sum_dict[sum(pizzas)] += 1

    for length in range(1, size):
        pizza_sum = sum(pizzas[:length])
        if pizza_sum <= selling_size:
            sum_dict[pizza_sum] += 1
        
        for start in range(size-1):
            pizza_sum = pizza_sum - pizzas[start] + pizzas[(start + length) % size]
            if pizza_sum <= selling_size:
                sum_dict[pizza_sum] += 1
    return sum_dict


def find_size(sum_list, finding_size, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if sum_list[mid][0] == finding_size:
        return mid
    elif sum_list[mid][0] > finding_size:
        return find_size(sum_list, finding_size, start, mid - 1)
    else:
        return find_size(sum_list, finding_size, mid + 1, end)


pizza_size = int(input())
m, n = map(int, input().split())
first_pizza = [int(input()) for _ in range(m)]
second_pizza = [int(input()) for _ in range(n)]

first_pizza_sum_dict = get_sum_dict(first_pizza, m, pizza_size)
second_pizza_sum_dict = get_sum_dict(second_pizza, n, pizza_size)
second_pizza_sum_list = sorted(second_pizza_sum_dict.items())

ans = 0
ans = ans + first_pizza_sum_dict[pizza_size] + second_pizza_sum_dict[pizza_size]

for first_pizza_sum, first_pizza_sum_count in first_pizza_sum_dict.items():
    required_second_pizza_size = pizza_size - first_pizza_sum
    index = find_size(second_pizza_sum_list, required_second_pizza_size, 0, len(second_pizza_sum_list)-1)
    if index >= 0:
        ans += first_pizza_sum_count * second_pizza_sum_list[index][1]

print(ans)