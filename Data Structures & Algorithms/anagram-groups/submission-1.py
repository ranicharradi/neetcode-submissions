class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        have={}
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            if s not in have:
                have[s] = [strs[i]]
                continue
            have[s].append(strs[i])
        return [*have.values()]