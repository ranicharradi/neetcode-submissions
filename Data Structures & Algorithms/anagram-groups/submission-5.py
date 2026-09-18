class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        have = defaultdict(list)
        for i, string in enumerate(strs):
            s = "".join(sorted(string))
            have[s].append(string)
        return [*have.values()]
        