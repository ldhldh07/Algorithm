def solution(plans):
    plans.sort(key=lambda plan: plan[1])
    length = len(plans)

    stack = []
    answer = []

    for i in range(length):
        if i == length - 1:
            answer.append(plans[i][0])
            while stack:
                answer.append(stack.pop()[0])
            continue

        current_start_time = Time(plans[i][1])
        next_start_time = Time(plans[i + 1][1])

        given_time = current_start_time.get_difference(next_start_time)
        left_time = try_solving(stack, answer, given_time, plans[i][0], plans[i][2])

        while left_time > 0 and stack:
            stacked_plan, rest_playtime = stack.pop()
            left_time = try_solving(stack, answer, left_time, stacked_plan, rest_playtime)

    return answer


class Time:
    def __init__(self, time):
        self.time = time
        self.hours = int(self.time[:2])
        self.minutes = int(self.time[-2:])

    def get_difference(self, next_time):
        return 60 * (next_time.hours - self.hours) + next_time.minutes - self.minutes


def try_solving(stack, answer, given_time, name, playtime):
    left_playtime = int(playtime) - given_time

    if left_playtime <= 0:
        answer.append(name)
        return -left_playtime
    else:
        stack.append((name, left_playtime))
        return 0