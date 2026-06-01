class Solution(object):
    def isValid(self, s):
        stack =[]
        mapping = {
            ")":"(",
            "}":"{",
            "]":"[",
        }
        for i in s:
            if i in mapping:
                if not stack or stack.pop() != mapping[i]:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0
obj = Solution()
s = input("Enter the parantheses : ")
result = obj.isValid(s)
print(result)
        