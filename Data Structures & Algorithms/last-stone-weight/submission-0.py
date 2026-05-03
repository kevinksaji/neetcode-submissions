class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        # heapify stones into a max heap
        # while the length of stones is more than 1, iterate the while loop
        negStones = []

        for stone in stones:
            negStones.append(-stone)

        
        
        heapq.heapify(negStones)

        while len(negStones) > 1:
            first = - heapq.heappop(negStones)
            second = - heapq.heappop(negStones)

            if first == second:
                continue
            else:
                second = abs(first - second)
                heapq.heappush(negStones, - second)

        if len(negStones) == 1:
            return - heapq.heappop(negStones)
        else:
            return 0

            


