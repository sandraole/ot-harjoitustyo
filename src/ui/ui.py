import tkinter as tk
from tkinter import ttk, messagebox
from ui.main import MainView
from ui.register import RegisterView
from services.book_service import BookService
from repositories.book_repository import BookRepository


class UI:
    def __init__(self, root, user_service):
        self._root = root
        self._user_service = user_service
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _clear_current_view(self):
        if self._current_view is not None:
            self._current_view.destroy()
            self._current_view = None

    def _show_login_view(self):
        self._clear_current_view()

        frame = tk.Frame(master=self._root, padx=10, pady=10)
        frame.pack(fill="both", expand=True)
        self._current_view = frame

        tk.Label(
            frame,
            text="Login",
            font=("Arial", 16)
        ).pack(pady=10)

        tk.Label(frame, text="Username").pack()
        username_entry = ttk.Entry(frame)
        username_entry.pack()

        tk.Label(frame, text="Password").pack()
        password_entry = ttk.Entry(frame, show="*")
        password_entry.pack()

        ttk.Button(
            frame,
            text="Sign In",
            command=lambda: self._sign_in(
                username_entry.get(),
                password_entry.get()
            )
        ).pack(pady=5)

        ttk.Button(
            frame,
            text="Register",
            command=self._show_register_view
        ).pack()

    def _sign_in(self, username, password):
        try:
            logged_in_username = self._user_service.login(username, password)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

        self._show_main_view(logged_in_username)

    def _show_main_view(self, username):
        self._clear_current_view()

        def logout_handler():
            self.start()

        safe_username = username.replace(" ", "_")
        file_path = f"data/{safe_username}_books.json"

        book_repository = BookRepository(file_path=file_path)
        book_service = BookService(book_repository=book_repository)

        main_view = MainView(
            root=self._root,
            username=username,
            logout_handler=logout_handler,
            book_service=book_service,
        )

        main_view.pack(fill="both", expand=True)
        self._current_view = main_view

    def _show_register_view(self):
        self._clear_current_view()

        def on_success():
            messagebox.showinfo("Success", "User created, you can log in now")
            self.start()

        def on_cancel():
            self.start()

        register_view = RegisterView(
            root=self._root,
            user_service=self._user_service,
            on_success=on_success,
            on_cancel=on_cancel,
        )

        register_view.pack(fill="both", expand=True)
        self._current_view = register_view
