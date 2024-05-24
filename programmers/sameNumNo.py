'''
같은 숫자는 싫어 - Level 1
arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
'''


def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        answer.append(arr[i])
        if arr[i] == arr[i-1]:
            answer.pop()
    return answer



n = [4,4,4,3,3]
print(solution(n))
