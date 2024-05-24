class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        letters_counter = Counter(letters)
        
        def can_make_word(w, ltrs_cnt):
            wrd_cnt = Counter(w)
            for i in w:
                if wrd_cnt[i] > ltrs_cnt[i]:
                    return False
            return True
        
        def get_word_score(w):
            out = 0
            for i in w:
                out += score[ord(i) - ord('a')]
            return out
            
        
        def helper(i):
            if i == len(words):
                return 0
            
            out = helper(i+1)
            
            if can_make_word(words[i], letters_counter):
                for x in words[i]:
                    letters_counter[x] -= 1
                
                out = max(out, get_word_score(words[i]) + helper(i+1))
                
                for x in words[i]:
                    letters_counter[x] += 1
            return out
        
        return helper(0)
        