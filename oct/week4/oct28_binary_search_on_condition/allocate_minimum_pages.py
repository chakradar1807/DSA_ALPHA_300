class Solution:
    def findPages(self, arr: list[int], k: int) -> int:
        if k > len(arr):
            return -1
        def countStudents(arr, page_limit):
            students = 1
            current_pages = 0
            for pages in arr:
                if current_pages + pages <= page_limit:
                    current_pages += pages
                else:
                    students += 1
                    current_pages = pages
            return students
                
        low = max(arr)
        high = sum(arr)
        ans = -1
            
        while low <= high:
            mid = low + (high - low) // 2
                
            if countStudents(arr, mid) <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
        
