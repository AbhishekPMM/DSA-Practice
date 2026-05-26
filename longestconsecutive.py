class Solution(object):

    def longestConsecutive(self, nums):

        s = set(nums)

        longest = 0

        for num in s:
            if num - 1 not in s:
                length = 1
                while num + length in s:
                    length += 1
                longest = max(longest, length)

        return longest

obj = Solution()
nums = list(map(int, input().split()))
result = obj.longestConsecutive(nums)
print(result)