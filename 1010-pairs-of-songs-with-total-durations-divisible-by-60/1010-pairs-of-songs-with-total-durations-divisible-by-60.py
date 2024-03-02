class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        paired_dict = defaultdict(int)
        for i in time:
            if not i%60:
                count += paired_dict[0]
            else:
                count += paired_dict[60-(i%60)]
            paired_dict[i%60] += 1
        return count
        