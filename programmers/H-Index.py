def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for idx in range(len(citations)):
        # 피인용수가 논문수와 같아지거나 피인용수가 논문수보다 작아지기 시작하는 숫자
        if citations[idx] < (idx + 1):
            return idx
    return len(citations)


citations = [0,1,2]
print(solution(citations))