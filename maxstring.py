#approach 1
'''class Solution(object):
    def maxSlidingWindow(self, nums, k):
        result=[]
        left = 0
        for right in range(len(nums)):
            if right-left+1 == k:
                result.append(max(nums[left:right+1]))
                left += 1
        return result
obj = Solution()
nums = list(map(int, input().split()))
k=int(input())
result = obj.maxSlidingWindow(nums,k)
print(result)'''

#approach 2
from collections import deque

class Solution(object):

    def maxSlidingWindow(self, nums, k):

        dq = deque()
        result = []

        for right in range(len(nums)):

            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            dq.append(right)

            if dq[0] < right - k + 1:
                dq.popleft()

            if right >= k - 1:
                result.append(nums[dq[0]])

        return result


obj = Solution()
nums = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter k: "))

result = obj.maxSlidingWindow(nums, k)

print(result)