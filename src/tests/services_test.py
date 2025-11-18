import unittest
import os
from services.user_service import UserService


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.test_file = "src/data/test_users.json"
        os.makedirs("src/data", exist_ok=True)

        self.user_service = UserService(self.test_file)

        with open(self.test_file, "w") as file:
            file.write("{}")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_user_success(self):
        self.user_service.create_user("testuser", "testpassword")
        self.assertTrue(self.user_service.authenticate(
            "testuser", "testpassword"))