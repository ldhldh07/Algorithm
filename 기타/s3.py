def can_be_measured(weights, target, left=[], right=[]):
    if len(weights) == 0:
        return (abs(sum(left) - sum(right)) == target)
    w = weights[0]
    return (can_be_measured(weights[1:], target, left+[w], right) or
            can_be_measured(weights[1:], target, left, right+[w]) or
            can_be_measured(weights[1:], target, left, right))


print(can_be_measured([1, 1, 5, 9], 7))  # True
print(can_be_measured([2, 5, 8, 9], 12)) # True
print(can_be_measured([1, 4, 10], 8))    # False
