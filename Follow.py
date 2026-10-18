class Follow:
    def __init__(self, follow_id: int, follower: Account, followee: Account):
        self.follow_id = follow_id
        self.follower = follower
        self.followee = followee

    def follow(self) -> "Follow":
        pass

    def unfollow(self) -> bool:
        pass

    def is_following(self, follower: Account, followee: Account) -> bool:
        pass