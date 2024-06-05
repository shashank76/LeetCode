class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counter = Counter(words[0])
        out = []
        
        for i in words[1:]:
            new_counter = Counter(i)
            for j in counter:
                counter[j] = min(counter[j], new_counter[j])
        
        for i in counter:
            for j in range(counter[i]):
                out.append(i)
        return out
        