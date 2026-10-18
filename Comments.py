class Comment:
    def __init__(self, comment_id: int, post: Post, author: Account):
        self.comment_id = comment_id
        self.post = post
        self.author = author