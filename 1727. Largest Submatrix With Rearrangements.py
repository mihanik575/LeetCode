# https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/

1
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row=len(matrix)
        col=len(matrix[0])
        result=0
        for r in range(1,row):
            for c in range(col):
                matrix[r][c]+=matrix[r-1][c] if matrix[r][c] else 0

        for r in range(row):
            matrix[r].sort(reverse=True)
            for c in range(col):
                result=max(result,(c+1)*matrix[r][c])
        return result