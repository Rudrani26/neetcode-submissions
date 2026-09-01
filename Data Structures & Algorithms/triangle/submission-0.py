class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #trying to solve by 1D, 2D is in leetcode
        n = len(triangle)
        
        for i in range(n-2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]
        