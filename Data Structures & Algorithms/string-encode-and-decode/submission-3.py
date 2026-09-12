class Solution:

    def encode(self, strs: List[str]) -> str:
        s = '\t'.join(strs) 
        print(1, strs)
        if strs==[]:
            return "\n"
        else: 
            return s
        
    def decode(self, s: str) -> List[str]:
        if s == "\n":
            return [] 
        strs = s.split('\t')
        print(2, strs)
        return strs