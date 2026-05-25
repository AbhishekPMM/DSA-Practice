#approach 1
"""class Solution(object):
    def productExceptSelf(self, nums):
        arr = []
        for i in range(len(nums)):
            result = 1
            for j in range(len(nums)):
                if j != i:
                    result *= nums[j]
                else:
                    continue
            arr.append(result)
        return arr
obj = Solution()
nums = list(map(int, input().split()))
res = obj.productExceptSelf(nums)
print(res)"""

#approach 2 using prefix and postfix
class Solution(object):
    def productExceptSelf(self, nums):
        a = len(nums)
        arr = [1] * a
        prefix = 1
        for i in range(a):
            arr[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(a-1, -1, -1):
            arr[i] *= postfix
            postfix *= nums[i]
        return arr
obj = Solution()
nums = list(map(int, input().split()))
result = obj.productExceptSelf(nums)
print(result)
