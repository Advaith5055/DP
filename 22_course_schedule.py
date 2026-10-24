def can_finish_courses(course_count, prerequisites):
    graph = [[] for _ in range(course_count)]
    indegree = [0] * course_count

    for course, prerequisite in prerequisites:
        graph[prerequisite].append(course)
        indegree[course] += 1

    available = [course for course in range(course_count) if indegree[course] == 0]
    completed = 0

    while available:
        course = available.pop()
        completed += 1

        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                available.append(next_course)

    return completed == course_count


assert can_finish_courses(2, [[1, 0]])
assert not can_finish_courses(2, [[1, 0], [0, 1]])
assert can_finish_courses(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
