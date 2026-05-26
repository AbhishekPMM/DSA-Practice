class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        n = len(nums)
        d=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    d.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    while left<right and nums[left]==nums[left-1]:
                        left +=1
                    while left<right and nums[right]==nums[right+1]:
                        right -= 1
                elif total<0:
                    left +=1
                else:
                    right -= 1
        return d
obj = Solution()
nums = list(map(int,input("enter the numbers :").split()))
result = obj.threeSum(nums)
print(result)