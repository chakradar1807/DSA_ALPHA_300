class Solution:
    def countFreq(self, arr : list[int],target : int) -> int:
        def findFirst(arr, target):
            low,high = 0, len(arr) - 1
            first = -1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == target:
                    first = mid
                    high = mid -1
                elif arr[mid] < target:
                    low = mid +1
                else:
                    high = mid - 1
            return first
        def findlast(arr, target):
            low, high = 0,len(arr)-1
            last = -1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == target:
                    last = mid
                    low = mid + 1
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return last
        first = findFirst(arr, target)
        if first == -1:
                return 0
                
        last = findlast(arr, target)
        return last - first + 1
                
