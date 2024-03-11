class Solution:
    def customSortString(self, order: str, s: str) -> str:
        out = defaultdict(int)
        i = 0
        for x in order:
            out[x]=i
            i+=1
        return "".join(sorted(s, key=lambda k:out.get(k,len(order))))
        