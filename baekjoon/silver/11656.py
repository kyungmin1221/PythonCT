import sys


def solution(s):
    answer = []
    result = []
    for i in range(len(s)):
        answer.append(s[i::])

    answer.sort()
    for i in range(len(answer)):
        result.append(answer[i])

    return result


s = sys.stdin.readline().strip()
ans = solution(s)
for i in ans:
    print(i)
