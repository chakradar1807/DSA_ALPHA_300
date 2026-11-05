class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res=nums[0]
        low=0
        high=len(nums)-1
        while low<high:
            mid=(high+low)//2
            if nums[mid]>nums[high]:
                low=mid+1
            else:
                high=mid
            res=min(res,nums[low])
            if low==high:
                break
        return res
