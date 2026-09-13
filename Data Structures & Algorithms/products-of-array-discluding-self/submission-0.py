class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            cpt=1
            for j in range(len(nums)):
                if i == j:
                    continue
                cpt *= nums[j]
            output.append(cpt)
        return output