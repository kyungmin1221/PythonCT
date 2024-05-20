import sys

n, m = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
S = [0] * n
C = [0] * m
answer = 0

S[0] = A[0]
for i in range(1, n):
    S[i] = S[i - 1] + A[i]

for i in range(n):
    div = S[i] % m
    if div == 0:
        answer += 1
    C[div] += 1

for i in range(m):
    # 조합 공식
    if C[i] > 0:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)



