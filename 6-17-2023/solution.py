class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        numList = [1] * len(nums)
        pre = 1
        post = 1
        for i in range(len(nums)):
            numList[i] *= pre
            numList[len(nums)-1-i] *= post
            pre *= nums[i]
            post *= nums[len(nums)-1-i]
        return numList