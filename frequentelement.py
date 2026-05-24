class Solution(object):
    def topKFrequent(self, nums, k):
        t = {}
        a = []
        for i in range(len(nums)):
            if nums[i] in t:
                t[nums[i]] += 1
            else:
                t[nums[i]] = 1
        x = sorted(t.items(), key = lambda x : x[1] , reverse =True)
        for j in range(k):
            a.append(x[j][0])
        return a
obj=Solution()
nums = list(map(int, input().split()))
k = int(input("k : "))
result = obj.topKFrequent(nums, k)
print(result)


            
            

