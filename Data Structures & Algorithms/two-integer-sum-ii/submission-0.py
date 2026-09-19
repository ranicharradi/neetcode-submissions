class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        have = {}
        for i, num in enumerate(numbers):
            if target - num in have: 
                return  [have[target - num]+1,i+1]
            have[num]=i
