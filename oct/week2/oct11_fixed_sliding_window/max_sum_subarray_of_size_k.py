class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        target_sum = threshold * k
        
        current_sum = 0
        for i in range(k):
            current_sum += arr[i]
            
        if current_sum >= target_sum:
            res += 1
            
        for r in range(k, len(arr)):
            current_sum = current_sum + arr[r] - arr[r - k]
            
            if current_sum >= target_sum:
                res += 1
                
        return res
