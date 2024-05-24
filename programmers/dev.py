import math

def solution(progresses, speeds):
    answer = []     # 정답 출력 배열
    new = []

    for i in range(len(progresses)):
        time = (100 - progresses[i]) / speeds[i]
        time = math.ceil(time)
        new.append(time)

    count = 1
    current_time = new[0]

    for i in range(1, len(new)):
        if current_time > new[i]:
            count += 1
        else:
            answer.append(count)
            count = 1
            current_time = new[i]

    answer.append(count)
    return answer

progress = [95,90,99,99,80,99]
speeds = [1,1,1,1,1,1]
a = solution(progress, speeds)
print(a)