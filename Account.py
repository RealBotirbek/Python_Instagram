class Account:
    def __init__(self, name: str, last_name: str, date_of_birth: str, username: str, phone_number: int, email: str, password: str):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.username = username
        self.phone_number = phone_number
        self.email = email
        self.password = password

    def login(self, email: str, password: str) -> bool:
        pass

    def logout(self) -> None:
        pass

    def update_profile(self, name: str | None, last_name: str | None, phone_number: str | None, email: str | None) -> None:
        pass

    def change_password(self, old_password: str, new_password: str) -> bool:
        pass

    # --- Social actions ---
    def create_post(self, title: str, content: str) -> "Post":
        return title, content

    def delete_post(self, post: "Post") -> bool:
        pass

    def edit_post(self, post: "Post", new_title: str, new_content: str) -> None:
        pass

    # --- Relationships ---
    def follow(self, user: "Account") -> None:
        pass

    def unfollow(self, user: "Account") -> None:
        pass

    def get_followers(self) -> list["Account"]:
        pass

    def get_following(self) -> list["Account"]:
        pass

    # --- Feed ---
    def get_feed(self) -> list["Post"]:
        pass