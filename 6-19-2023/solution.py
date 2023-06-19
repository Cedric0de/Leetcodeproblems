class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        string = ""
        for stri in strs:
            string += str(len(stri)) + ";" + stri
        return string
        pass

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        string, i = [], 0

        while i < len(str):
            j=i
            while str[j] != ";":
                j+=1
            length = int(str[i:j])
            string.append(str[j+1:j+1+length])
            i = j+1+length
        return string
        pass