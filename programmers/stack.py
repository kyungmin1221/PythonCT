def solution(s):
    result =[]
    for char in s:
        if char == '(':
            result.append(char)
        else:    # ) 일 경우
            if not result:
                return False
            result.pop()
    if result:
        return False

    return True


s = '()()'
print(solution(s))
