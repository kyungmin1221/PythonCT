# 섬의 개수 - BFS

from collections import deque
import sys

# 상하좌우 탐색을 위한 전역변수 설정
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def house(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < width and land[nx][ny] == 1:
                land[nx][ny] = 0
                queue.append((nx, ny))


while True:
    width, height = map(int, sys.stdin.readline().split())
    land = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
    count = 0

    if width == 0 and height == 0:
        break

    for i in range(height):
        for j in range(width):
            if land[i][j] == 1:
                house(i, j)
                count += 1
    print(count)