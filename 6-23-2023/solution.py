class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in tokens:
            if i == '+':
                second = stack.pop()
                first = stack.pop()
                stack.append(first+second)
            elif i == '-':
                second = stack.pop()
                first = stack.pop()
                stack.append(first-second)
            elif i == '*':
                second = stack.pop()
                first = stack.pop()
                stack.append(first*second)
            elif i == '/':
                second = stack.pop()
                first = stack.pop()
                stack.append(int(float(first)/second))
            else:
                stack.append(int(i))
        return stack[-1]