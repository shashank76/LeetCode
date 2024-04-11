class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        out = [0]*len(deck)
        q = deque(range(len(deck)))
        for i in deck:
            x = q.popleft()
            out[x] = i
            if q:
                q.append(q.popleft())   
        return out
            
        