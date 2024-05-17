import collections

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams["".join(sorted(word))].append(word)

        return list(anagrams.values())


if __name__ == "__main__":
    solution = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams(input_strs)
    print(result)
