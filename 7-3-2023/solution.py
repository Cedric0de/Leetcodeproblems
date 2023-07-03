class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n=len(nums)-1
        s=0
        while s<=n:
            i = s + ((n-s)//2)
            if nums[i] > target:
                n=i-1
            elif nums[i] < target:
                s=i+1
            else:
                return i
        return -1