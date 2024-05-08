class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse = True)
        placed = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i) for i in range(4, len(score) + 1)]
        num_to_award = {num : award for num, award in zip(sorted_scores, placed)}
        results = [num_to_award[i] for i in score]
        return results