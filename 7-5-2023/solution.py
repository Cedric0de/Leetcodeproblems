class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left=1
        right=max(piles)
        k=right
        while left<=right:
            m = (left+right)//2
            hours = 0
            for p in piles:
                hours += ((p-1)//m)+1

            if hours<=h:
                k = min(k,m)
                right = m-1
            else:
                left = m+1
        return k