class Solution(object):
    def twosum(self, nums, target):

        n = len(nums)
        left = 0
        right = n - 1
        while left<right:
            Total = nums[left] + nums[right]
            if Total == target:
                return [left+1,right+1]
            elif Total<target:
                left += 1
            else:
                right -= 1
obj = Solution()
nums = list(map(int, input("enter the numbers : ").split()))
target = int(input("enter the target: "))
result = obj.twosum(nums,target)
print(result)




