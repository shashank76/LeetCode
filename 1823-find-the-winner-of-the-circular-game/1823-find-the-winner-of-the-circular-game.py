class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1,n+1)]
        i = 0
        j = n
        while j > 1:
            for x in range(1, k + 1):
                if i > j-1:
                    i = i - j
                i += 1
            friends.remove(friends[i-1])
            i-=1
            j-=1
        return friends[0]