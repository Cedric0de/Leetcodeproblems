class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        curr = 1
        temp = 1
        if len(nums) == 0:
            curr=0
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                temp += 1
                curr = max(curr,temp)
            elif nums[i] == nums[i+1]:
                curr = max(curr,temp)
            else:
                temp=1
                curr = max(curr,temp)
            
        return curr