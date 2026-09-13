class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        y = sorted(set(nums))
        nums = list(y)
        cpt = 0
        saved = 0
        for i in range(len(nums)-1): 
            if nums[i+1] == nums[i] + 1:
                cpt += 1
            else:
                saved = max(cpt, saved)
                cpt = 0
                continue
        saved = max(cpt, saved)
        return saved + 1
