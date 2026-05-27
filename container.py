class Solution(object):
    def container(self,height):
        n=len(height)
        left = 0
        right = n-1
        maxarea=0
        while left<right:
            k = min(height[left],height[right])*(right-left)
            maxarea=max(maxarea,k)
            if height[left]<height[right]:
                left +=1
            else:
                right -= 1
        return maxarea
obj = Solution()
hieght = list(map(int,input("enter the heights : ").split()))
result = obj.container(hieght)
print(result)