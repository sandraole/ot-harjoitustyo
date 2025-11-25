import json
import os


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

    def _save_users(self):
        directory = os.path.dirname(self._file_path)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as e:
                print(f"Could not create directory {directory}: {e}")
        try:
            with open(self._file_path, "w", encoding="utf-8") as file:

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


user_service = UserService()
