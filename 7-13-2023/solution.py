class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left=0
        right=len(nums)-1
        while left<=right:
            m = (left+right)//2
            if((target>nums[m] or nums[left]>target) and nums[left]<=nums[m]):
                left=m+1
            elif(target<=nums[m] and nums[left]<=target and nums[left]<=nums[m]):
                right=m-1
            elif((target<nums[m] or target>nums[right]) and nums[left]>nums[m]):
                right=m-1
            else:
                left=m+1
            if(nums[m]==target):
                return m
        return -1