def solution(targets):
    targets.sort(key = lambda x: [x[1], x[0]])
    answer = 0
    
    shot_spot = 0
    
    for target in targets:
        if target[0] >= shot_spot:
            answer += 1
            shot_spot = target[1]

    return answer 