class Solution:
    def search(self, nums: List[int], target: int) -> int:
        toul = len(nums)
        l = 0
        r = toul - 1

        while (r >= l):
            mid = l + (r - l) // 2 
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else: 
                return mid
        
        return -1


