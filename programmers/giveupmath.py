def solution(answers):
    result = []
    correct_1 = [1,2,3,4,5]
    correct_2 = [2,1,2,3,2,4,2,5]
    correct_3 = [3,3,1,1,2,2,4,4,5,5]
    answer = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == correct_1[i % len(correct_1)]:
            answer[0] += 1
        if answers[i] == correct_2[i % len(correct_2)]:
            answer[1] += 1
        if answers[i] == correct_3[i % len(correct_3)]:
            answer[2] += 1

    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i + 1)

    return result


# answer = [1,2,3,4,5]
answer = [1,3,2,4,2]
print(solution(answer))