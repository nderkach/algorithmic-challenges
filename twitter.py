class User(object):

    def __init__(self, userId):
        self.userId = userId
        self.follows = []


class Tweet(object):

    def __init__(self, tweetId, userId):
        self.tweetId = tweetId
        self.userId = userId


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.feed = []
        self.users = {}

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        if userId not in self.users:
            self.users[userId] = User(userId)

        self.feed.append(Tweet(tweetId, userId))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """

        if userId in self.users:

            current_user = self.users[userId]

            print(current_user.follows)
            print([self.users[post.userId] for post in self.feed])

            print([post for post in self.feed if self.users[post.userId] in current_user.follows])

            posts_in_feed = [post.tweetId for post in self.feed[
                ::-1] if (self.users[post.userId] in current_user.follows or post.userId == current_user.userId)]

            return posts_in_feed[-1:-11:-1]

        else:
            return []

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """

        if followerId in self.users:
            follower = self.users[followerId]
        else:
            follower = User(followerId)
            self.users[followerId] = follower
        if followeeId in self.users:
            followee = self.users[followeeId]
        else:
            followee = User(followeeId)
            self.users[followeeId] = followee

        follower.follows.append(followee)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """

        if followerId in self.users and followeeId in self.users:
            follower = self.users[followerId]
            followee = self.users[followeeId]
            if followee in follower.follows:
                follower.follows.remove(followee)


# Your Twitter object will be instantiated and called as such:
t = Twitter()
t.postTweet(1, 5)
print(t.getNewsFeed(1))
t.follow(1, 2)
t.postTweet(2, 6)
print(t.getNewsFeed(1))


