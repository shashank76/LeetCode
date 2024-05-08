class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse = True)
        placed = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        for i in range(3, len(score)):
            placed.append(str(i+1))
            
        ranks_with_score = {num : award for num, award in zip(sorted_scores, placed)}
        out = [ranks_with_score[i] for i in score]
        return out