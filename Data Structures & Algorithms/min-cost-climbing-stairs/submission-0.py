class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #we increase the length of cost to include the position past cost which is our destination
        # cost = [1,2,3]  => cost = [1,2,3, 0]
        cost.append(0)

        #we start from the end and from a position which gives us both +1 step and +2 step
        #we wont get that from the last (target position) or from the one before that as it would give only +1 step
        for i in range(len(cost) - 3, -1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
            #cost[i] += min(cost[i+1],cost[i+2])
        
        return min(cost[0], cost[1])
        
        