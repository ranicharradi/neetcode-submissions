class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        have = defaultdict(list)
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            have[s].append(strs[i])
        return [*have.values()]
        