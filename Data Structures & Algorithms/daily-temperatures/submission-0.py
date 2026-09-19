class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        output = [0]*len(temps)
        for i in range(len(temps)-2, -1, -1):
            j = i+1
            while temps[i] >= temps[j] and output[j] > 0:
                    j += output[j]
            if temps[i] < temps[j]:
                output[i] = j - i
        return output