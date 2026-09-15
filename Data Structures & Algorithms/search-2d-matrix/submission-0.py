class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        left = 0
        right = m - 1
    
        while (right >= left):
            middle = left + (right - left) // 2 
            if  matrix[middle][-1] >= target >= matrix[middle][0]:
                break
            elif matrix[middle][-1] < target:
                left = middle + 1
            else:
                right = middle - 1
        nums = matrix[middle]
        left = 0
        right = len(nums) - 1

        while (right >= left):
            mid = left + (right - left) // 2 
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return True

        return False
        



      