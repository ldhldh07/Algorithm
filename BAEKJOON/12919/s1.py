import sys
sys.setrecursionlimit(10**6)

def order_case(count_a, count_b, operation_order):
    if not count_a and not count_b:
        order_case_list.append(operation_order)
        return
    if count_a:
        order_case(count_a - 1, count_b, operation_order + [0])
    if count_b:
        order_case(count_a, count_b -1, operation_order + [1])


S, T = input(), input()

count_A_of_S = 0
count_B_of_S = 0
count_A_of_T = 0
count_B_of_T = 0

for ch in S:
    if ch == 'A':
        count_A_of_S += 1
    else:
        count_B_of_S += 1

for ch in T:
    if ch == 'A':
        count_A_of_T += 1
    else:
        count_B_of_T += 1

answer = 0

order_case_list = []
order_case(count_A_of_T - count_A_of_S, count_B_of_T - count_B_of_S, [])
for order in order_case_list:
    current_word = S
    for operation in order:
        if not operation:
            current_word += 'A'
        else:
            current_word += 'B'
            current_word = current_word[::-1]
    if current_word == T:
        answer = 1
        break

print(answer)
