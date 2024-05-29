from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(len(computers))]
    for idx in range(n):
        if not visited[idx]:
            BFS(idx, visited, n, computers)
            answer += 1

    return answer

def BFS(idx , visited, n, computers):
    queue = deque()
    queue.append(idx)
    while queue:
        idx = queue.popleft()
        visited[idx] = 1
        for a in range(n):
            if computers[idx][a] and not visited[a]:
                queue.append(a)

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
