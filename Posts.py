class Post:
    def __init__(self, owner: Account, title: str, content: str):
        self.owner = owner
        self.title = title
        self.content = content

    # --- Content management ---
    def edit_post(self, new_title: str, new_content: str) -> None:
        pass

    def delete_post(self) -> None:
        pass

    # --- Engagement (basic structure even if not fully implemented yet) ---
    def like_post(self, user: Account) -> None:
        pass

    def unlike_post(self, user: Account) -> None:
        pass

    def get_likes_count(self) -> int:
        pass

    # --- Ownership / checks ---
    def is_owner(self, user: Account) -> bool:
        pass

    # --- Info retrieval ---
    def get_summary(self) -> dict:
        pass