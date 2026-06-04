class Solution(object):
    def evalRPN(self, tokens):

        stack = []

        for i in tokens:

            if i == "+":
                b = stack.pop()
                a = stack.pop()
                stack.append(a + b)

            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)

            elif i == "*":
                b = stack.pop()
                a = stack.pop()
                stack.append(a * b)

            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(float(a) / b))

            else:
                stack.append(int(i))

        return stack[-1]

obj = Solution()

tokens = input("Enter tokens separated by space: ").split()

result = obj.evalRPN(tokens)

print(result)