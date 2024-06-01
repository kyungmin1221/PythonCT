# def solution(nums):
#     unique_types = len(set(nums))
#
#     if len(nums) // 2 > unique_types:
#         return unique_types
#     else:
#         return len(nums) // 2
def solution(nums):
    answer = 0
    dict = {}
    for char in nums:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1

    # dict = { (1:2), (2,1), (3,2) }
    if len(nums) // 2 > len(dict):
        answer = len(dict)
        return answer
    else:
        answer = len(nums) // 2
        return answer


nums = [1,2,3,1,1,1]
print(solution(nums))
