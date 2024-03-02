class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {}
        for h, w in rectangles:
            count[h/w] = 1+ count.get(h/w, 0)
        out = 0
        for i in count.values():
            if i > 1:
                out += (i * (i-1)) // 2
        return out
            
        