def solution(array, commands):
    answer = []
    result = []
    for i in range(len(commands)):
        a = commands[i][0] - 1  # 2 -> 1
        b = commands[i][1] - 1  # 5 -> 4
        c = commands[i][2] - 1  # 3 -> 2
        for j in range(a, b+1):
            result.append(array[j])
        result.sort()
        answer.append(result[c])
        result = []


    return answer


array = [1,5,2,6,3,7,4]
commands = [ [2,5,3], [4,4,1], [1,7,3]]
a = solution(array, commands)
print(a)
