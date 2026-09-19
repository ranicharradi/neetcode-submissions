class Solution:
    def trap(self, h: List[int]) -> int:
        l = 0
        r = len(h) - 1
        bhim = bhim2 = 0
        output = 0
        while l <= r:
            if h[l] < h[r]:
                bhim = max(bhim, h[l])
                output += bhim - h[l]
                l += 1
            else:
                bhim2 = max(bhim2, h[r])
                output += bhim2 - h[r]
                r -= 1  
        return output




