from collections import defaultdict

def solution(arrows):
    answer = 0
    move = [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)]
    visited_nodes = defaultdict(int)
    visited_edges = defaultdict(int)
    
    x, y = 0, 0
    visited_nodes[(x, y)] = 1

    for arrow in arrows:
        for _ in range(2):  # 대각선 이동 시 중간점 처리를 위해 2번 이동
            nx, ny = x + move[arrow][0], y + move[arrow][1]
            if visited_nodes[(nx, ny)] and not visited_edges[(x, y, nx, ny)]:
                answer += 1
            visited_nodes[(nx, ny)] = 1
            visited_edges[(x, y, nx, ny)] = 1
            visited_edges[(nx, ny, x, y)] = 1
            x, y = nx, ny
    return answer
