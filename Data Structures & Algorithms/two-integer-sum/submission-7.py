class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        have = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in have: 
                return  [have[target - nums[i]],i]
            have[nums[i]]=i


                