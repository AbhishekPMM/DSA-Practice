class Solution(object):
    def checkInclusion(self, s1, s2):
        x = len(s1)
        y = len(s2)
        dt1 = {}
        dt2 = {}
        if x>y:
            return False
        for i in s1:
            dt1[i] = dt1.get(i,0) + 1
        for i in range(x):
            dt2[s2[i]] = dt2.get(s2[i],0)+1
        if dt1 == dt2:
            return True
        left = 0 
        for i in range(x,y):
            dt2[s2[i]] = dt2.get(s2[i],0)+1
            dt2[s2[left]] -= 1
            if dt2[s2[left]] == 0:
                del dt2.s2[left]
            left +=1
            if dt2 == dt1:
                return True
        return False
obj = Solution()
s1=input("Enter the string to ckeck : ")
s2=input("Enter the string : ")
result = obj.checkInclusion(s1,s2)
print(result)