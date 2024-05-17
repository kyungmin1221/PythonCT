class Solution(object):
    def threeSum(self, nums):
        results = []
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            if nums[i] == 0 and nums[left] == 0 and nums[right] == 0:
                results.append([nums[i], nums[left], nums[right]])
                break

            # 중복된 결과 이므로 결과에서 제외하기 위함
            if nums[i] == nums[i - 1]:
                continue

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 0]
    result = solution.threeSum(nums)
    print(result)
