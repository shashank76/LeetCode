class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(list)
        self.followers = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.count, tweetId])
        self.count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        out  = []
        minHeap = []
        
        self.followers[userId].add(userId)
        
        for followeeId in self.followers[userId]:
            if followeeId in self.tweets:
                idx = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][idx]
                minHeap.append([count, tweetId, followeeId, idx-1])
        
        heapq.heapify(minHeap)
        
        while minHeap and len(out) < 10:
            count, tweetId, followeeId, idx = heapq.heappop(minHeap)
            out.append(tweetId)
            if idx >= 0:
                count, tweetId = self.tweets[followeeId][idx]
                heapq.heappush(minHeap, [count, tweetId, followeeId, idx-1])
        return out        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)