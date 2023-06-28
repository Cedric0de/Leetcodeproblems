class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        first = 0
        second = len(s) - 1
        while first<second:
            if not s[first].isalnum():
                first+=1
            elif not s[second].isalnum():
                second-=1
            elif s[first].lower()!=s[second].lower():
                return False
            else:
                first+=1
                second-=1
        return True