# 단어 뒤집기 2

import sys

data = sys.stdin.readline().strip()

stack = []
answer = ''
flag = False    # 괄호안의 여부를 체크
for d in data:
    if d == '<':
        flag = True
        while stack:
            answer += stack.pop()
        answer += d
        continue
    stack.append(d)

    if d == '>':
        flag = False
        while stack:
            answer += stack.pop(0)

    if d == ' ' and not flag:
        for i in range(len(stack)):
            if i == 0:
                stack.pop()
                continue
            answer += stack.pop()
        answer += ' '

while stack:
    answer += stack.pop()

print(answer)






