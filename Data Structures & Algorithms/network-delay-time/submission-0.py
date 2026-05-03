class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # create a dictionary that stores nodes as keys and neighbours as edges, build adjacency list

        adjList = defaultdict(list)

        for u, v, ti in times:
            adjList[u].append((v, ti))

        
        # create a heap and run dijkstra's algorithm

        # insert initial node and cost into heap

        q = [(0, k)]

        visited = set()

        time = 0

        while q:

            # get the node with smallest cost

            cost, node = heapq.heappop(q)

            if node in visited:
                continue

            time = max(cost, time)

            visited.add(node)

            # insert neighbours into heap

            for nei in adjList[node]:
                neiNode, neiCost = nei
                if neiNode not in visited:
                    heapq.heappush(q, (neiCost + cost, neiNode))

        return time if len(visited) == n else -1

                

