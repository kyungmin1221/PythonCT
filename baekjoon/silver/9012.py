import sys

def bracket():
    answer = list(sys.stdin.readline().strip())
    result = []
    for i in range(len(answer)):
        if answer[i] == '(':
            result.append(answer[i])
        elif answer[i] == ')':
            if len(result) == 0:
                result.append(answer[i])
                break
            else:
                result.pop()
    if len(result) > 0:
        return "NO"
    else:
        return "YES"

t = int(sys.stdin.readline().strip())
for _ in range(t):
    print(bracket())
