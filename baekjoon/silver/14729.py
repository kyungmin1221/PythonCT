'''
<메모리 초과 발생>

import sys
import heapq

n = int(sys.stdin.readline().strip())
result = []
for i in range(n):
    grade = str(sys.stdin.readline().strip())
    heapq.heappush(result, grade)

a = 0
while result:
    a += 1
    if a == 8:
        break
    print(heapq.heappop(result))
'''

import sys
import heapq

n = int(sys.stdin.readline().strip())
result = []
for i in range(n):
    grade = float(sys.stdin.readline().strip())
    heapq.heappush(result, grade)

for i in range(7):
    print('{:.3f}'.format(heapq.heappop(result)))

