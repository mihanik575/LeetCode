# https://leetcode.com/problems/pascals-triangle-ii/description/


class Solution(object):
    def getRow(self, rowIndex):

        result = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                result[i - j] += result[i - j - 1]
        return result