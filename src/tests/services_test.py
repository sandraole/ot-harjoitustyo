import unittest
import os
from services.user_service import UserService


class TestUserService(unittest.TestCase):

    def setUp(self):
        self.test_file = "src/data/test_users.json"
        os.makedirs("src/data", exist_ok=True)

        if os.path.exists(self.test_file):
            os.remove(self.test_file)

        with open(self.test_file, "w", encoding="utf-8") as file:
            file.write("{}")

        self.user_service = UserService(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_create_user_success(self):
        self.user_service.create_user("testuser", "testpassword")
        self.assertTrue(self.user_service.authenticate("testuser", "testpassword"))

    def test_create_user_and_reject_empty_username(self):
        with self.assertRaises(ValueError):
            self.user_service.create_user("   ", "password")

    def test_create_user_and_reject_empty_password(self):
        with self.assertRaises(ValueError):
            self.user_service.create_user("username", "   ")

    def test_create_user_existing_username(self):
        self.user_service.create_user("testuser", "password")
        with self.assertRaises(ValueError):
            self.user_service.create_user("testuser", "otherpassword")

    def test_login_success_returns_username(self):
        self.user_service.create_user("testuser", "password")
        result = self.user_service.login("testuser", "password")
        self.assertEqual(result, "testuser")

    def test_login_empty_username(self):
        with self.assertRaises(ValueError):
            self.user_service.login("", "password")

    def test_login_empty_password(self):
        with self.assertRaises(ValueError):
            self.user_service.login("username", "")

    def test_login_wrong_password(self):
        self.user_service.create_user("testuser", "password")
        with self.assertRaises(ValueError):
            self.user_service.login("testuser", "wrongpassword")

    def test_authenticate_returns_true_for_correct_username_or_password(self):
        self.user_service.create_user("testuser", "password")
        self.assertTrue(self.user_service.authenticate("testuser", "password"))

    def test_authenticate_returns_false_for_incorrect_username_or_password(self):
        self.user_service.create_user("testuser", "password")
        self.assertFalse(self.user_service.authenticate("testuser", "wrongpassword"))
        self.assertFalse(self.user_service.authenticate("unknownuser", "password"))

    def test_load_users_file_not_found(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        service = UserService(self.test_file)
        self.assertEqual(service._users, {})

    def test_load_users_invalid_to_empty_file(self):
        with open(self.test_file, "w", encoding="utf-8") as file:
            file.write("{ invalid json")
        service = UserService(self.test_file)
        self.assertEqual(service._users, {})

    def test_save_users_to_file(self):
        self.user_service.create_user("testuser", "password")
        new_service = UserService(self.test_file)
        self.assertTrue(new_service.authenticate("testuser", "password"))
