class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0
        total = 0
        left = 0
        leftm=height[left]
        right=len(height)-1
        rightm=height[right]
        while left<right:
            if leftm < rightm:
                left+=1
                leftm = max(leftm,height[left])
                total += leftm - height[left]
            else:
                right-=1
                rightm = max(rightm, height[right])
                total += rightm - height[right]
            
        return total