class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        most = 0
        left = 0
        right = len(height)-1
        while right>left:
            if (height[left]>=height[right]):
                total=height[right] * (right-left)
                right-=1
            elif (height[left]<height[right]):
                total=height[left] * (right-left) 
                left+=1
            if total>most:
                    most = total
        return most