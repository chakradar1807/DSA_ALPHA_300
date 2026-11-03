class Solution:
    def findFloorAndCeil(self, arr: list[int], x: int) -> tuple[int, int]:
        # 1. Find Floor (largest element <= x)
        low, high = 0, len(arr) - 1
        floor_ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] <= x:
                floor_ans = mid
                low = mid + 1
            else:
                high = mid - 1

        # 2. Find Ceil (smallest element >= x)
        low, high = 0, len(arr) - 1
        ceil_ans = -1
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] >= x:
                ceil_ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return (floor_ans, ceil_ans)
