import sys

n = int(sys.stdin.readline())
num = list(sys.stdin.readline().strip())
sum = 0

for i in num:
    sum += int(i)

print(sum)