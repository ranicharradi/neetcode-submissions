class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        cpt = 1
        zero = 0
        for i in nums:
            if i == 0:
                zero += 1
                continue
            cpt *= i
        if zero >= 2:
            return [0]*len(nums)
        if zero == 1:
            for j in nums:
                if j != 0:
                    output.append(0)
                    continue
                output.append(cpt)
        if zero ==0:
            for k in nums:
                output.append(cpt//k)

        return output