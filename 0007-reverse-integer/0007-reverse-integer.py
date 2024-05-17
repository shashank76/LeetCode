class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False

        if x < 0:
            is_negative = True
            x = -x
        
        str_val = str(x)
        out = ""
        n = len(str_val)
        i = n - 1
        while i >= 0:
            out += str_val[i]
            i -= 1
        x = int(out)
        
        if is_negative:
            x = -x
        
        if x < -2 ** 31 or x > 2 ** 31 - 1:
            x = 0
        
        return x