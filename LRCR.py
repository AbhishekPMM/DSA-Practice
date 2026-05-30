class Solution(object):

    def characterReplacement(self, s, k):

        count = {}

        left = 0
        maxFreq = 0
        result = 0

        for right in range(len(s)):

            count[s[right]] = count.get(s[right], 0) + 1

            maxFreq = max(maxFreq, count[s[right]])

            while (right - left + 1) - maxFreq > k:

                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result
obj = Solution()
s = input("")
k = int(input())
result = obj.characterReplacement(s,k)
print(result)