class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        have = set()
        nums.sort()
        output = []
        for i in range(1, len(nums)):
            have.add(nums[i-1]) 
            for j in range(i+1, len(nums)):
                target= - (nums[i] + nums[j])
                if target in have:
                    output.append((nums[i], nums[j], target)) 
        return list(set(output))

