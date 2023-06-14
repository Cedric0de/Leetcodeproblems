class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
            hashmap.update({nums[i]:i})
        
        for i in nums:
            if target-i == i and nums.index(i) != hashmap[i]:
                return [nums.index(i), hashmap[i]]
            if target-i in hashmap and nums.index(i) != hashmap[target-i]:
                return [nums.index(i),nums.index(target-i)]