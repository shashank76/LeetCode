class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        merged_dict = Counter((s1+ " " +s2).rsplit())
        out = []
        for key in merged_dict.keys():
            if merged_dict[key] == 1:
                out.append(key)
        return out
        