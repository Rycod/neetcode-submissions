class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        midr = len(matrix)//2
        midc = len(matrix[0])//2
        lr, lc, rr, rc = 0, 0, len(matrix)-1, len(matrix[0])-1
        tr = 0
        while lr <= rr:
            midr = (lr + rr)//2
            if matrix[midr][0] <= target and matrix[midr][-1] >= target:
                tr = midr
                break
            elif matrix[midr][0] > target:
                rr -= 1
            else:
                lr += 1
        print(tr)
        while lc <= rc:
            midc = (lc+rc)//2
            if matrix[tr][midc] == target:
                return True
            if matrix[tr][midc] > target:
                rc -= 1
            else:
                lc += 1
        return False