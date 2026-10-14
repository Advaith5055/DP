def daily_temperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []

    for day, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            previous_day = stack.pop()
            answer[previous_day] = day - previous_day
        stack.append(day)

    return answer


assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
