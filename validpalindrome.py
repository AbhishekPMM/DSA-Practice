class Solution(object):
    def validPlindrome(self, strs):
        n = len(strs)
        left = 0
        right = n-1
        while left < right:
            while left < right and not strs[left].isalnum():
                left += 1
            while left < right and not strs[right].isalnum():
                right -= 1
            if strs[left].lower() != strs[right].lower():
                return False
            left += 1
            right -= 1
        return True
obj = Solution()
strs = input("enter the string : ")
result = obj.validPlindrome(strs)
print(result)

