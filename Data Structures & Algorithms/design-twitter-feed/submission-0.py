from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.users = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        #increment global time counter
        # add (time, tweetId) to tweets[userIds] list
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:

        max_heap = []
        res = []

        followees = self.users[userId] or {userId}
        followees.add(userId)

        for followee in followees:
            tweets = self.tweets[followee]
            if tweets:
                last_index = len(tweets) - 1 
                time, tweet_id = tweets[last_index]
                heapq.heappush(max_heap,(-time, tweet_id, followee, last_index))

        while max_heap and len(res) < 10:
            time,tweet_id,user,last_index = heapq.heappop(max_heap)
            res.append(tweet_id)

            if last_index > 0:
                prev_index = last_index - 1
                prev_time, prev_tweet_id = self.tweets[user][prev_index]
                heapq.heappush(max_heap, (-prev_time, prev_tweet_id, user, prev_index))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # add followeeId to users[followerID] set if the ids are not the same
        if followerId != followeeId:
            self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # remove followeeId fom users[followerID] if followeeId is in the followers set
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)