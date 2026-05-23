class solution(object):
    def isAnagram(self, s, t):
        sfreq = {}
        vfreq = {}
        for i in s:
            sfreq[i] = sfreq.get(i, 0) + 1
        for j in t:
            vfreq[j] = vfreq.get(j, 0) + 1
        if sfreq == vfreq:
            return True
        else:
            return False
obj = solution()
s = input("s: ")
t = input("t: ")

result = obj.isAnagram(s, t)
print(result)