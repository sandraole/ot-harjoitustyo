import json
from data.file_utils import open_for_write


class UserService:
    def __init__(self, file_path="data/users.json"):
        self._file_path = file_path
        self._users = {}
        self._load_users()

    def _load_users(self):
        try:
            with open(self._file_path, "r", encoding="utf-8") as file:
                self._users = json.load(file)
        except FileNotFoundError:
            self._users = {}
        except json.JSONDecodeError:
            self._users = {}

    def _save_users(self):
        try:
            with open_for_write(self._file_path) as file:
                json.dump(self._users, file)
        except OSError as e:
            print(f"Failed to save users: {e}")

    def create_user(self, username, password):
        if username in self._users:
            raise ValueError("User already exists")
        self._users[username] = password
        self._save_users()

    def authenticate(self, username, password):
        return self._users.get(username) == password
