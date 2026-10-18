class View:
    def __init__(self, view_id: int, post: Post, user: Account):
        self.view_id = view_id
        self.post = post
        self.user = user

    def record_view(self) -> "View":
        pass

    def has_viewed(self, user: Account, post: Post) -> bool:
        pass