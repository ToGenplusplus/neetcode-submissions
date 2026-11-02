from collections import defaultdict
from heapq import heappush, heappop
 
class Twitter:

    def __init__(self):
        self.time = 0
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:

        users = self.users[userId] or {userId}
        users.add(userId)

        max_heap = []
        
        for user in users:
            tweets = self.tweets[user]
            if tweets:
                last_index = len(tweets) - 1
                time, tweetId = tweets[last_index]
                heappush(max_heap, (-time, tweetId, user, last_index))

        res = []

        while max_heap and len(res) < 10:
            time, tweetId, user, last_index = heappop(max_heap)
            res.append(tweetId)

            if last_index > 0:
                nxt_index = last_index - 1
                prev_time, prev_tweetId = self.tweets[user][nxt_index]
                heappush(max_heap, (-prev_time, prev_tweetId, user, nxt_index))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)
        
