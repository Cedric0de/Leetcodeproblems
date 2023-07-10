class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right=len(nums)-1
        res=nums[left]
        while left<=right:
            if nums[left]<nums[right]:
                res = min(res,nums[left])
                break
            m = (left+right)//2
            res = min(res,nums[m])
            if(nums[left]<=nums[m]):
                left=m+1
            else:
                right=m-1
        return res