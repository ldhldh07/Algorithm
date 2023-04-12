from pprint import pprint

R, C, N = map(int, input().split())

square = [list(input()) for _ in range(R)]
bomb_count = [[0 for _ in range(C)] for _ in range(R)]


pprint(square)
pprint(bomb_count)
