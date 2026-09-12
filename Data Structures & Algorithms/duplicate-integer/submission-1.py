class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        y = len(set(nums))
        x = len(nums)
        return bool (x - y)
