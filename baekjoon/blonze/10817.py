import sys

a, b, c = map(int, sys.stdin.readline().split())
result = []
result.append(a)
result.append(b)
result.append(c)
result.sort(reverse=True)

print(result[1])
