class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        def check(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        ans = ''
        for i in range(0, len(s)):
            ans = max(ans, check(i, i), check(i, i + 1), key=len)
        return ans


if __name__ == "__main__":
    solution = Solution()
    input_strs = 'bac'
    result = solution.longestPalindrome(input_strs)
    print(result)