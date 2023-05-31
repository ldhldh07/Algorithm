import sys
sys.setrecursionlimit(10**6)

preorder = []

def preorder_to_postorder(pre):
    left = []
    right = []
    for index, value in enumerate(pre):
        if not index:
            route = value
        else:
            if value < route:
                left.append(value)
            else:
                right.append(value)
    if len(left):
        if len(left) == 1:
            print(left[0])
        else:
            preorder_to_postorder(left)
    if len(right):
        if len(right) == 1:
            print(right[0])
        else:
            preorder_to_postorder(right)
    print(route)


while True:
    try:
        preorder.append(int(input()))
    except EOFError:
        break

preorder_to_postorder(preorder)