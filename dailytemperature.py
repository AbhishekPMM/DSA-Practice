class Solution(object):
    def dailyTemperatures(self, temp):
        result = [0]*len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[i]>temp[stack[-1]]:
                oldindex = stack.pop()
                result[oldindex] = i - oldindex
            stack.append(i)
        return result
obj = Solution()
temp = list(map(int,input("enter the temperature : ").split()))
result = obj.dailyTemperatures(temp)
print(result)
