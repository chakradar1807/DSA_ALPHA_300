class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            max_row = 0
            
            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
                    
            left_bigger = mid > 0 and mat[max_row][mid - 1] > mat[max_row][mid]
            right_bigger = mid < n - 1 and mat[max_row][mid + 1] > mat[max_row][mid]
            
            if not left_bigger and not right_bigger:
                return [max_row, mid]
            elif left_bigger:
                high = mid - 1
            else:
                low = mid + 1
                
        return [-1, -1]
        
