from collections import defaultdict
import copy

N = int(input())
weights = list(map(int, input().split()))


checkable_weights = defaultdict(int)
for weight in weights:
    cws = list(checkable_weights.keys())
    for checkable_weight in cws:
        checkable_weights[abs(checkable_weight-weight)] = 1
        checkable_weights[abs(checkable_weight+weight)] = 1
    checkable_weights[weight] = 1

check_N = int(input())
check_weights = list(map(int, input().split()))
ans_list = []
for check_weight in check_weights:
    ans_list.append('Y' if checkable_weights[check_weight] else 'N')

print(*ans_list)