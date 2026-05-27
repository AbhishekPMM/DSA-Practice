class Solution(object):
    def trap(self, height):
        n=len(height)
        left = 0
        right = n-1
        water = 0
        leftmax = 0
        rightmax = 0
        while left < right:
            if height[left]<height[right]:
                if height[left]>=leftmax:
                    leftmax = height[left]
                else:
                    water += leftmax - height[left]
                left += 1
            else:
                if height[right]>=rightmax:
                    rightmax = height[right]
                else:
                    water += rightmax - height[right]
                right -= 1
        return water


obj = Solution()
height = list(map(int, input("enter the height : ").split()))
result = obj.trap(height)
print(result)
            

