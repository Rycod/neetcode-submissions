class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        currR, currC, currS = defaultdict(set), defaultdict(set), defaultdict(set)
        for r in range(9):
            for c in range(9):
                e = board[r][c]
                if e == '.':
                    continue
                s = 3*(r//3) + (c//3)
                if e in currR[r] or e in currC[c] or e in currS[s]:
                    return False
                currR[r].add(e)
                currC[c].add(e)
                currS[s].add(e)
        return True