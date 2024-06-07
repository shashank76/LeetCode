class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split()
        for d in dictionary:
            for i in range(len(sentence)):
                if sentence[i].startswith(d):
                    sentence[i] = d
        return " ".join(sentence)
        