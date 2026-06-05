class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:

            if i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)

            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)

            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(float(b)/a))
            
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            else:
                stack.append(int(i))
        return stack[-1]
obj = Solution()

tokens = input("Enter tokens separated by space: ").split()

result = obj.evalRPN(tokens)

print(result)