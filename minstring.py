class Solution(object):
    def minstring(self,s,t):
        if len(s)<len(t):
            return ""
        dt1 = {}
        dt2 = {}
        for i in t:
            dt1[i] = dt1.get(i,0) + 1
        result = [-1,-1]
        have = 0
        minlen = float('inf')
        need = len(dt1)
        left = 0
        for right in range(len(s)):
            c=s[right]
            dt2[c] = dt2.get(c,0)+1
            if c in dt1 and dt2[c] == dt1[c]:
                have += 1
            while(have == need):
                if (right-left + 1) < minlen:
                    minlen = right - left + 1
                    result = [left,right]
                dt2[s[left]] -= 1
                if s[left] in dt1 and dt2[s[left]]<dt1[s[left]]:
                    have -= 1
                left += 1
        l,r = result
        if minlen == float('inf'):
            return ""
        return s[l:r+1]
obj = Solution()
s = input("enter the string : ")
t = input("enter the string to check : ")
result = obj.minstring(s,t)
print(result)    