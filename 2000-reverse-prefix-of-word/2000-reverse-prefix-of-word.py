class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch in word:
            word = list(word)
            i, j = 0, word.index(ch)
            while i < j:
                temp = word[i]
                word[i] = word[j]
                word[j] = temp
                i +=1
                j-=1
            return ''.join(word)
        else:
            return word
        