class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        out=[]
        for name, height in sorted(zip(names, heights), key=lambda x:x[1], reverse=True):
            out.append(name)
        return out
        