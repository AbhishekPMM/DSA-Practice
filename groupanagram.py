class Solution(object):
    def groupAnagrams(self, strs):
        dt = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in dt:
                dt[key] = []
            dt[key].append(i)
        return list(dt.values())
obj = Solution()
s = input("enter the array: ").split()
result = obj.groupAnagrams(s)

print(result)