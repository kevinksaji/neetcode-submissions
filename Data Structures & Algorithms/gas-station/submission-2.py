class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = 0
        i = 0
        total = 0

        if sum(gas) < sum(cost):
            return -1
        
        while i < len(gas):

            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                res = i + 1
            
            i += 1

        if res > len(gas):
            return -1

        return res
