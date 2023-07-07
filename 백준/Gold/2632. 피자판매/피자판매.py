from collections import defaultdict

def get_sum_dict(pizzas, size, selling_size):
    sum_dict = defaultdict(int)
    total_pizza_sum = sum(pizzas)
    if total_pizza_sum <= selling_size:
        sum_dict[total_pizza_sum] += 1

    for length in range(1, size):
        pizza_sum = sum(pizzas[:length])
        if pizza_sum <= selling_size:
            sum_dict[pizza_sum] += 1
        
        for start in range(size-1):
            pizza_sum = pizza_sum - pizzas[start] + pizzas[(start + length) % size]
            if pizza_sum <= selling_size:
                sum_dict[pizza_sum] += 1
    return sum_dict


pizza_size = int(input())
m, n = map(int, input().split())
first_pizza = [int(input()) for _ in range(m)]
second_pizza = [int(input()) for _ in range(n)]

first_pizza_sum_dict = get_sum_dict(first_pizza, m, pizza_size)
second_pizza_sum_dict = get_sum_dict(second_pizza, n, pizza_size)

ans = 0
ans = ans + first_pizza_sum_dict[pizza_size] + second_pizza_sum_dict[pizza_size]

for first_pizza_sum, first_pizza_sum_count in first_pizza_sum_dict.items():
    required_second_pizza_size = pizza_size - first_pizza_sum
    ans += first_pizza_sum_count * second_pizza_sum_dict[required_second_pizza_size]

print(ans)