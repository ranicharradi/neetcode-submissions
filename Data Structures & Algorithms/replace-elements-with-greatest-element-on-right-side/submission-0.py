class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        x = len(arr)
        for i in range(x):
            mx=-1
            for j in range(i+1, x):
                mx=max(arr[j], mx)
            arr[i] = mx   
            print(arr)
        return arr