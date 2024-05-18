# 1. 오름차순 방법
class Solution(object):
    def arrayPairSum(self, nums):
        results = []
        nums.sort()
        sum = 0

        for i in nums:
            results.append(i)
            if len(results) == 2:
                sum += min(results)
                results = []
        return sum



# 2. 짝수 번째 값 계산
class Solution(object):
    def arrayPairSum(self, nums):

        nums.sort()
        sum = 0

        for i, n in enumerate(nums):
            if i % 2 == 0:
                sum += n
        return sum

# 3. 파이썬 한줄
class Solution(object):
    def arrayPairSum(self, nums):
        return sum(sorted(nums)[::2])



if __name__ == "__main__":
    solution = Solution()
    nums = [1, 4, 3, 5]
    result = solution.arrayPairSum(nums)
    print(result)
