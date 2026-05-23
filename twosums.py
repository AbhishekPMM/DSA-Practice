#first logic try
"""class Solution(object):
    def twoSum(self, nums, target):
        j=0
        v=1
        for i in range(len(nums) - 1):
            if nums[j] + nums[v] == target:
                return [j,v]
            else:
                v +=1
                continue #i only tested the adjacent elements
"""
#2nd approach
"""class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i] + nums[k] == target:
                    return [i,k]
                else:
                    continue"""

#3rd approach(optimal)
class Solution(object):
    def twoSum(self, nums, target):
        dt = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dt:
                return [i,dt[diff]]
            else:
                dt[nums[i]] = i

obj = Solution()

nums = list(map(int, input().split()))
target = int(input("Target: "))

result = obj.twoSum(nums, target)
print(result)

