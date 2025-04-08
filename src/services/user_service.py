import json


class UserService:
    def __init__(self, file_path="data/users.json"):
        self._file_path = file_path
        self._users = {}
        self._load_users()

    def _load_users(self):
        try:
            with open(self._file_path, "r") as file:
                self._users = json.load(file)
        except FileNotFoundError:
            self._users = {}

    def _save_users(self):
        with open(self._file_path, "w") as file:
            json.dump(self._users, file)

    def create_user(self, username, password):
        if username in self._users:
            raise Exception("User already exists")
        self._users[username] = password
        self._save_users()

    def authenticate(self, username, password):
        return self._users.get(username) == password


user_service = UserService()
