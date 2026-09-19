class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        A = []
        B = []
        for num in nums:
            if num >= 0:
                A.append(num **2)
                continue
            B.append(num **2)
        B = B[::-1]
        l = r = 0
        output = []
        while l < len(B) or r < len(A):
            if r >= len(A) or (l < len(B) and B[l] < A[r]): 
                output.append(B[l])
                l+=1
            else:
                output.append(A[r])
                r+=1
        return output
            