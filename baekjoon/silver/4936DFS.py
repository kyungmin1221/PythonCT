import sys
sys.setrecursionlimit(10 ** 6)    # 재귀 깊이 제한을 변경 ,  파이썬의 재귀 최대 깊이의 기본 설정이 1,000회

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def house(x, y):
    visited[x][y] = 1

    if land[x][y] == 1:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < height and 0 <= ny < width and land[nx][ny] == 1 and not visited[nx][ny]:
                house(nx, ny)


while True:
    width, height = map(int, sys.stdin.readline().split())
    land = [list(map(int, sys.stdin.readline().split())) for _ in range(height)]
    visited = [[0] * width for _ in range(height)]
    count = 0

    if width == 0 and height == 0:
        break

    for i in range(height):
        for j in range(width):
            if land[i][j] == 1 and not visited[i][j]:
                house(i, j)
                count += 1
    print(count)
