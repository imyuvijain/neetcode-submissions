class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = nums.copy()

        for i, num in enumerate(nums[2:]):
            i = i+2
            print(f"\n{i, num=}")

            paths = []

            for j in range(2,i+1): #  1 2
                print(f"{i,j=}")
                
                paths.append(memo[i-j])
                print(f"{paths=}")

            if paths: memo[i] += max(paths)
        
        print(f"{memo=}")
        return max(memo)
