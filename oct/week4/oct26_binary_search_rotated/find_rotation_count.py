class Solution:
    def findKRotation(self, arr: list[int]) -> int:
        low, high = 0, len(arr) - 1

        while low < high:
            mid = low + (high - low) // 2

            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid

        return low
