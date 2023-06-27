class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        total = 0
        for i, h in enumerate(heights):
            start=i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                total = max(height*(i-index),total)
                start = index
            stack.append((start,h))
        for i, h in stack:
            total = max(total, h*(len(heights)-i))
        return total
