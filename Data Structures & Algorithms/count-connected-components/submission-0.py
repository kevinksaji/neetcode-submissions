import collections
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        # create an adjacency list

        visited = set()
        adjList = collections.defaultdict(list)
        connected_components = 0

        for edge in edges:
            u, v = edge[0], edge[1]

            adjList[u].append(v)
            adjList[v].append(u)


        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for connected in adjList[node]:
                dfs(connected)


        for i in range(n):

            if i not in visited:
                connected_components += 1
                dfs(i)

        return connected_components