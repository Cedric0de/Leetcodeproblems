class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashfreq = {}
        for elem in nums:
            if elem not in hashfreq:
                hashfreq[elem] = 1
            else:
                hashfreq[elem] += 1
        numbers = [0] * k
        for i in range(k):
            num = max(hashfreq, key=hashfreq.get)
            numbers[i] = num
            del hashfreq[num]
        return numbers