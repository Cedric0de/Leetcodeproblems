class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for i in range(len(strs)):
            sorstring = sorted(strs[i])
            if "".join(sorstring) not in hashmap:
                hashmap["".join(sorstring)] = []
            hashmap["".join(sorstring)].append(strs[i])
        
        return list(hashmap.values())