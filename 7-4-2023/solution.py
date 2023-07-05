class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        bot = row-1
        while top<=bot:
            curr = (top+bot)//2
            if matrix[curr][-1]<target:
                top = curr+1
            elif matrix[curr][0]>target:
                bot=curr-1
            else:
                break

        if not (top<=bot):
            return False
            
        curr = (top+bot)//2
        l,r=0,col-1
        while l<=r:
            m=(l+r)//2
            if target>matrix[curr][m]:
                l = m+1
            elif target<matrix[curr][m]:
                r = m-1 
            else:
                return True
        return False    