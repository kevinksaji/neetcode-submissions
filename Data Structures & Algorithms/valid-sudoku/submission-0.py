class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def noDupes(cells):
            seen = set()

            for v in cells:
                if v == ".":
                    continue

                if v in seen:
                    return False
                seen.add(v)
            return True


        for r in range(9):
            if not noDupes(board[r]):
                return False

        
        for c in range(9):
            col = [board[r][c] for r in range(9)]

            if not noDupes(col):
                return False

        for br in range(0, 9, 3):
            for bc in range(0, 9, 3):
                block = [board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)]

                if not noDupes(block):
                    return False

        return True

