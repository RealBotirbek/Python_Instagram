class Like:
    def __init__(self, like_id: int, post: Post, user: Account):
        self.like_id = like_id
        self.post = post
        self.user = user

    def create(self) -> "Like":
        pass

    def remove(self) -> bool:
        pass