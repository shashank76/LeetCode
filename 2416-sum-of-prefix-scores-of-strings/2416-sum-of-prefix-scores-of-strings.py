class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = lambda: defaultdict(trie)
        t = trie()
        for word in words:
            current = t
            for char in word:
                if not char in current:
                    current[char]['count'] = 0
                current = current[char]
                current['count'] += 1
        answer = [0]*len(words)
        for i,word in enumerate(words):
            current = t
            for char in word:
                current = current[char]
                answer[i] += current['count']
        return answer
        