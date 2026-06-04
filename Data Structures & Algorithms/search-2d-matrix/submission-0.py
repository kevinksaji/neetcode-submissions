class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROW, COL = len(matrix), len(matrix[0])


        b, t = 0, ROW-1

        row = None
        

        while b <= t:
            mid = b + (t-b) // 2

            if matrix[mid][0] <= target and matrix[mid][COL-1] >= target:
                row = matrix[mid]
                break

            elif matrix[mid][0] >= target:
                t = mid - 1

            else:
                b = mid + 1


        if not row:
            return False
        
        print(row)
        l, r = 0, COL -1

        while l <= r:
            mid = l + (r-l) // 2

            if row[mid] == target:
                return True

            elif row[mid] < target:
                l = mid + 1

            else:
                r = mid -1

        return False




            

        