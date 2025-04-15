import tkinter as tk
from tkinter import messagebox

class MainView(tk.Frame):
    def __init__(self, root):
        super().__init__(root, padx=10, pady=10)
        self.pack()

        tk.Label(self, text="Welcome to your Budget!", font=("Arial", 16)).pack(pady=5)

        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Expense:").grid(row=0, column=0, sticky="w")
        self.expense_entry = tk.Entry(form_frame, width=30)
        self.expense_entry.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(form_frame, text="Amount (€):").grid(row=1, column=0, sticky="w")
        self.amount_entry = tk.Entry(form_frame, width=15)
        self.amount_entry.grid(row=1, column=1, padx=5, pady=2)

        add_button = tk.Button(form_frame, text="Add Expense", command=self.add_expense)
        add_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.expense_listbox = tk.Listbox(self, width=50, selectmode=tk.SINGLE)
        self.expense_listbox.pack(pady=10)

        remove_button = tk.Button(self, text="Remove Selected Expense", command=self.remove_expense)
        remove_button.pack(pady=5)

        self.expenses = []

    def add_expense(self):
        expense = self.expense_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if not expense or not amount:
            messagebox.showwarning("Warning", "Please fill in both fields!")
            return

        try:
            amount_val = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the amount!")
            return

        expense_text = f"{expense}: {amount_val:.2f} €"
        self.expenses.append((expense, amount_val))

        self.expense_listbox.insert(tk.END, expense_text)

        self.expense_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def remove_expense(self):
        selected = self.expense_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select an expense to remove!")
            return

        index = selected[0]
        
        self.expense_listbox.delete(index)
        del self.expenses[index]