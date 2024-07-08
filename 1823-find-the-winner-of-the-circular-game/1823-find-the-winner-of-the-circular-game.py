class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [i for i in range(1,n+1)]
        i = 0
        while n > 1:
            for x in range(1, k + 1):
                if i > len(friends) - 1:
                    i = i - len(friends)
                i += 1
            n -= 1
            friends.remove(friends[i-1])
            i -= 1
        return friends[0]