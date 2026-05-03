from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # create a dictionary called prereq that stores each course mapped to prereq courses as a list of courses as the value

        prereq = defaultdict(list)

        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # create visited set to track cycles
        visited = set()
        completed = set()

        def dfs(crs):

            if crs in completed:
                return True

            if crs in visited:
                return False

            visited.add(crs)

            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            visited.remove(crs)
            completed.add(crs)
            return True


        for i in range(numCourses):

            if not dfs(i):
                return False

        return True

        



        