class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        out = score = 0
        tokens.sort()
        l, r = 0, len(tokens)-1
        while l <= r:
            if power >= tokens[l]:
                power-= tokens[l]
                score+=1
                l+= 1
                out = max(out, score)
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                break
        return out
        