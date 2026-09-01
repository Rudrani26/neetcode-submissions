class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #number of houses
        n = len(costs)

        #if no house then return 0
        if not costs:
            return 0
        
        for i in range(1, n):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][0], costs[i-1][1])
        
        min_cost = min(costs[n-1][0], costs[n-1][1], costs[n-1][2])
        
        return min_cost