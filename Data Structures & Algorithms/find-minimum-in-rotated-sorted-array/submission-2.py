class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return (min(nums))
        
        L, R = 0, len(nums) - 1
        
        while L < R:
            mid = L + (R-L)//2
            print(f"Before: {L=} {mid=} {R=}")
            

            if nums[mid+1] < nums[mid]:
                return (nums[mid+1])
            else:
                if nums[mid] > nums[R]:
                    L = mid
                else:
                    R = mid
        return nums[L]