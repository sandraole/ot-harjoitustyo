"""Moduuli joka vastaa käyttäjiin liittyvästä sovelluslogiikasta."""

import json
from data.file_utils import open_for_write


class UserService:
    """Luokka joka vastaa käyttäjien luomisesta ja kirjautumisesta.

    Käyttäjät tallennetaaj sanakirjana JSON-tiedostoon.
    Avaimena toimii käyttäjätunnut ja arvona salasana.

    Attributes:
        _file_path: JSON-tiedoston polku, johon käyttäjät tallennetaan.
        _users: Muistissa pidettävä sanakirja käyttäjätunnuksista ja salasanoista.
    """

    def __init__(self, file_path="data/users.json"):
        """"Luo uuden User_service olion.

        Args:
            file_path: tiedoston polku, mihin tallennetaan käyttäjät.
        """
        self._file_path = file_path
        self._users = {}
        self._load_users()

    def _load_users(self):
        """Lataa JSON-tiedostosta käyttäjäy.

        Jos tiedostoa ei ole tai se on virheellinen, tehdään uusi sanakirja.
        """
        try:
            with open(self._file_path, "r", encoding="utf-8") as file:
                self._users = json.load(file)
        except FileNotFoundError:
            self._users = {}
        except json.JSONDecodeError:
            self._users = {}

    def _save_users(self):
        """Tallentaa käyttäjät JSON-tiedstoon."""
        try:
            with open_for_write(self._file_path) as file:
                json.dump(self._users, file)
        except OSError as e:
            print(f"Failed to save users: {e}")

    def create_user(self, username, password):
        """Jos käyttäjätunnus on vapaa -- > luodaan uusi käyttäjätunnus.

        Args:
            username: käyttäjätunnus.
            password: salasana.

        Raises:
            ValueError: Jos käyttäjätunnus on jo käytössä, jos tunnus tai salasana
            puuttuvat.
        """
        username = username.strip()
        password = password.strip()

        if not username or not password:
            raise ValueError("Username and password are required")

        if username in self._users:
            raise ValueError("User already exists")

        self._users[username] = password
        self._save_users()

    def authenticate(self, username, password):
        """Varmistaa vastaavatko käyttäjätunnus ja salasana toisiaan.

        Args:
            username: käyttäjätunnus.
            passwors: salasana.

        Returns:
            True, jos tunnus ja salasana täsmäävät, muuten False.
        """
        return self._users.get(username) == password

    def login(self, username, password):
        """"Kirjaa käyttäjän sisään.

        Args:
            username: käyttäjätunnus.
            passwors: salasana.

        Returns:
            Kirjautuneen käyttäjän tunnus.

        Raises:
            ValueError:
                Jos kirjautuminen epäonnistuu tai tunnus/salasana tyhjä.
        """
        username = username.strip()
        password = password.strip()

        if not username or not password:
            raise ValueError("Username and password are required")

        if self._users.get(username) != password:
            raise ValueError("Invalid username or password")

        return username
