from pydantic import BaseModel
import hashlib

class AppUser(BaseModel):
    id: int
    name: str
    password: str

    def hash_password(self) -> int:
        self.password = hashlib.new("sha256", bytes(self.password, encoding="utf-8")).hexdigest()

    def check_password(self, pw: str) -> bool:
        return self.password == hashlib.new("sha256", bytes(pw, encoding="utf-8")).hexdigest()

class UserSystem(BaseModel):
    users: list[AppUser] = []

    def add_user(self, user: AppUser) -> None:
        user.hash_password()
        self.users.append(user)

    def get_user(self, name: str) -> AppUser:
        return list(filter(lambda u: u.name == name, self.users))[0]
