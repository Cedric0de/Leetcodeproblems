class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        lis = [0] * len(temperatures)
        stack = []
        for i,x in enumerate(temperatures):
            while stack and x > stack[-1][0]:
                stackT, stackInd = stack.pop()
                lis[stackInd] = (i - stackInd)
            stack.append([x,i])
        return lis