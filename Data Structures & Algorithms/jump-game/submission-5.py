class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False for i in range(len(nums))]

        if memo:
            memo[-1] = True

        for i in range(len(nums[-2::-1])):

            index = len(nums)-(i+2)

            print(index)

            if nums[index]==0:
                memo[index]=False
                continue

            for j in range(1,nums[index]+1):
                if index+j < len(nums):
                    print(f" {index=} {nums[index]=}->{index+j=}")
                    if memo[index+j]:
                        memo[index] = True
                        break
                print()
        print(memo)
        return memo[0]

